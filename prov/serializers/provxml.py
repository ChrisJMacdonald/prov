"""PROV-XML serializers for ProvDocument

"""
__author__ = 'Lion Krischer'
__email__ = 'krischer@geophysik.uni-muenchen.de'

import logging
from lxml import etree

logger = logging.getLogger(__name__)

import prov
import prov.constants

NS_PROV = "http://www.w3.org/ns/prov#"
NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"


class ProvXMLException(prov.Error):
    pass


class ProvXMLSerializer(prov.Serializer):
    def serialize(self, stream, **kwargs):
        # Build the namespace map for lxml and attach it to the root XML
        # element.
        nsmap = {ns.prefix: ns.uri for ns in
                 self.document._namespaces.get_registered_namespaces()}
        if self.document._namespaces._default:
            nsmap[None] = self.document._namespaces._default.uri
        nsmap["prov"] = NS_PROV

        xml_root = etree.Element(_ns_prov("document"), nsmap=nsmap)

        # Filter functions used to sort the attributes according to the
        # PROV-XML specification.
        filter_fcts = [
            lambda x: x[0] in prov.constants.PROV_ATTRIBUTE_QNAMES,
            lambda x: x[0] in prov.constants.PROV_ATTRIBUTE_LITERALS,
            lambda x: x[0] == prov.constants.PROV_LABEL,
            lambda x: x[0] == prov.constants.PROV_LOCATION,
            lambda x: x[0] == prov.constants.PROV_ROLE,
            lambda x: x[0] == prov.constants.PROV_TYPE,
            lambda x: x[0] == prov.constants.PROV_VALUE,
            lambda x: True
        ]

        for record in self.document._records:
            rec_type = record.get_type()
            rec_label = prov.constants.PROV_N_MAP[rec_type]
            identifier = unicode(record._identifier)

            elem = etree.SubElement(
                xml_root, _ns_prov(rec_label),
                {_ns_prov("id"): identifier})

            used_attributes = []
            for fct in filter_fcts:
                _fct = lambda x: x not in used_attributes and fct(x) \
                                 and x[1] is not None
                for attr, value in filter(_fct, record.attributes):
                    used_attributes.append((attr, value))
                    subelem = etree.SubElement(
                        elem, _ns(attr.namespace.uri, attr.localpart))
                    if isinstance(value, prov.model.Literal):
                        subelem.attrib[_ns_xsi("type")] = "%s:%s" % (
                            value.datatype.namespace.prefix,
                            value.datatype.localpart)
                        value = value.value
                    else:
                        value = str(value)
                    subelem.text = value

        print ""
        print etree.tostring(xml_root, pretty_print=True)


    def deserialize(self, stream, **kwargs):
        raise NotImplementedError


def _ns(ns, tag):
    return "{%s}%s" % (ns, tag)


def _ns_prov(tag):
    return _ns(NS_PROV, tag)

def _ns_xsi(tag):
    return _ns(NS_XSI, tag)
