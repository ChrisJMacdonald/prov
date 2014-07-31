"""
PROV-XML serializers for ProvDocument
"""
__author__ = 'Lion Krischer'
__email__ = 'krischer@geophysik.uni-muenchen.de'

import datetime
import logging
from lxml import etree
import warnings

logger = logging.getLogger(__name__)

import prov
from prov.model import PROV_REC_CLS
from prov.constants import *

NS_PROV = "http://www.w3.org/ns/prov#"
NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
NS_XSD = "http://www.w3.org/2001/XMLSchema"
NS_XML = "http://www.w3.org/XML/1998/namespace"


def sorted_attributes(element, attributes):
    """
    Helper function sorting attributes into the order required by PROV-XML.
    """
    attributes = list(attributes)
    order = list(PROV_REC_CLS[element].FORMAL_ATTRIBUTES)

    # Append label, location, role, type, and value attributes. This is
    # universal amongst all elements.
    order.extend([PROV_LABEL, PROV_LOCATION, PROV_ROLE, PROV_TYPE,
                  PROV_VALUE])

    sorted_elements = []
    for item in order:
        this_type_list = []
        for e in list(attributes):
            if e[0] != item:
                continue
            this_type_list.append(e)
            attributes.remove(e)
        this_type_list.sort(key=lambda x: (str(x[0]), str(x[1])))
        sorted_elements.extend(this_type_list)
    # Add remaining attributes. According to the spec, the other attributes
    # have a fixed alphabetical order.
    attributes.sort(key=lambda x: (str(x[0]), str(x[1])))
    sorted_elements.extend(attributes)

    return sorted_elements


class ProvXMLException(prov.Error):
    pass


class ProvXMLSerializer(prov.Serializer):
    def serialize(self, stream, force_types=False, **kwargs):
        """
        :param stream: Where to save the output.
        :type force_types: boolean, optional
        :param force_types: Will force xsd:types to be written for most
            attributes mainly only PROV-"attributes", e.g. tags not in the
            PROV namespace. Off by default meaning xsd:type attributes will
            only be set for prov:type, prov:location, and prov:value as is
            done in the official PROV-XML specification.
        """
        # Build the namespace map for lxml and attach it to the root XML
        # element. No dictionary comprehension in Python 2.6!
        nsmap = dict((ns.prefix, ns.uri) for ns in
                     self.document._namespaces.get_registered_namespaces())
        if self.document._namespaces._default:
            nsmap[None] = self.document._namespaces._default.uri
        # Add the prov, XSI, and XSD namespaces by default.
        nsmap["prov"] = NS_PROV
        nsmap["xsi"] = NS_XSI
        nsmap["xsd"] = NS_XSD

        xml_root = etree.Element(_ns_prov("document"), nsmap=nsmap)

        for record in self.document._records:
            rec_type = record.get_type()
            rec_label = PROV_N_MAP[rec_type]
            identifier = unicode(record._identifier) \
                if record._identifier else None

            if identifier:
                attrs = {_ns_prov("id"): identifier}
            else:
                attrs = None

            elem = etree.SubElement(xml_root, _ns_prov(rec_label), attrs)

            for attr, value in sorted_attributes(rec_type, record.attributes):
                subelem = etree.SubElement(
                    elem, _ns(attr.namespace.uri, attr.localpart))
                if isinstance(value, prov.model.Literal):
                    if value.datatype not in \
                            [None, PROV["InternationalizedString"]]:
                        subelem.attrib[_ns_xsi("type")] = "%s:%s" % (
                            value.datatype.namespace.prefix,
                            value.datatype.localpart)
                    if value.langtag is not None:
                        subelem.attrib[_ns(NS_XML, "lang")] = value.langtag
                    v = value.value
                elif isinstance(value, datetime.datetime):
                    v = value.isoformat()
                else:
                    v = str(value)

                # xsd type inference.
                #
                # This is a bit messy and there are all kinds of special
                # rules but it appears to get the job done.
                #
                # If it is a type element and does not yet have an
                # associated xsi type, try to infer it from the value.
                # The not startswith("prov:") check is a little bit hacky to
                # avoid type interference when the type is a standard prov
                # type.
                if (force_types or attr in [PROV_TYPE, PROV_LOCATION,
                                            PROV_VALUE]) and \
                        _ns_xsi("type") not in subelem.attrib and \
                        not str(value).startswith("prov:") and \
                        not (attr in PROV_ATTRIBUTE_QNAMES and v) and \
                        attr not in [PROV_ATTR_TIME, PROV_LABEL]:
                    xsd_type = None
                    if isinstance(value, (str, unicode)):
                        xsd_type = XSD_STRING
                    elif isinstance(value, float):
                        xsd_type = XSD_DOUBLE
                    elif isinstance(value, int):
                        xsd_type = XSD_INT
                    elif isinstance(value, bool):
                        xsd_type = XSD_BOOLEAN
                    elif isinstance(value, datetime.datetime):
                        xsd_type = XSD_DATETIME
                    elif isinstance(value, prov.identifier.Identifier):
                        xsd_type = XSD_ANYURI

                    if xsd_type is not None:
                        subelem.attrib[_ns_xsi("type")] = str(xsd_type)

                if attr in PROV_ATTRIBUTE_QNAMES and v:
                    subelem.attrib[_ns_prov("ref")] = v
                else:
                    subelem.text = v

        et = etree.ElementTree(xml_root)
        et.write(stream, pretty_print=True, xml_declaration=True,
                 encoding="UTF-8")

    def deserialize(self, stream, **kwargs):
        xml_doc = etree.parse(stream).getroot()

        # Remove all comments.
        for c in xml_doc.xpath("//comment()"):
            p = c.getparent()
            p.remove(c)

        document = prov.model.ProvDocument()
        self.deserialize_subtree(xml_doc, document)
        return document

    def deserialize_subtree(self, xml_doc, bundle):
        for key, value in xml_doc.nsmap.items():
            bundle.add_namespace(key, value)

        # No dictionary comprehension in Python 2.6.
        r_nsmap = dict((value, key) for (key, value) in xml_doc.nsmap.items())

        for element in xml_doc:
            qname = etree.QName(element)
            if qname.namespace == NS_PROV:
                # Ignore the <prov:other> element storing non-PROV information.
                if qname.localname == "other":
                    warnings.warn(
                        "Document contains non-PROV information in "
                        "<prov:other>. It will be ignored in this package.",
                        UserWarning)
                    continue

                rec_type = PROV_RECORD_IDS_MAP[qname.localname]

                id_tag = _ns_prov("id")
                rec_id = element.attrib[id_tag] if id_tag in element.attrib \
                    else None

                # Recursively build bundles.
                if rec_type == PROV_BUNDLE:
                    new_bundle = prov.model.ProvBundle(document=bundle)
                    self.deserialize_subtree(element, new_bundle)
                    bundle.add_bundle(new_bundle,
                                      new_bundle.valid_qualified_name(rec_id))

                attributes = []
                other_attributes = []
                for subel in element:
                    sqname = etree.QName(subel)
                    if sqname.namespace == NS_PROV:
                        _t = PROV[sqname.localname]
                        d = attributes
                    else:
                        _t = "%s:%s" % (r_nsmap[sqname.namespace],
                                        sqname.localname)
                        d = other_attributes

                    if len(subel.attrib) > 1:
                        raise NotImplementedError
                    elif len(subel.attrib) == 1:
                        key, value = subel.attrib.items()[0]
                        if key == _ns_xsi("type"):
                            _v = prov.model.Literal(
                                subel.text,
                                XSD[value.split(":")[1]])
                        elif key == _ns_prov("ref"):
                            _v = value
                        elif key == _ns(NS_XML, "lang"):
                            _v = prov.model.Literal(subel.text, langtag=value)
                        else:
                            raise NotImplementedError
                    else:
                        _v = subel.text
                    d.append((_t, _v))

                if _ns_xsi("type") in element.attrib:
                    value = element.attrib[_ns_xsi("type")]
                    other_attributes.append((PROV["type"], value))

                bundle.new_record(rec_type, rec_id, attributes,
                                  other_attributes)
            else:
                raise NotImplementedError
        return bundle


def _ns(ns, tag):
    return "{%s}%s" % (ns, tag)


def _ns_prov(tag):
    return _ns(NS_PROV, tag)


def _ns_xsi(tag):
    return _ns(NS_XSI, tag)
