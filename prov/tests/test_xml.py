import difflib
import glob
import inspect
import io
from lxml import etree
import os
import unittest

import prov.model as prov


EX_NS = ('ex', 'http://example.com/ns/ex#')
EX_TR = ('tr', 'http://example.com/ns/tr#')

# Most general way to get the path.
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(
    inspect.currentframe()))), "xml")


def compare_xml(doc1, doc2):
    """
    Helper function to compare two XML files. It will parse both once again
    and write them in a canonical fashion.
    """
    try:
        doc1.seek(0, 0)
    except AttributeError:
        pass
    try:
        doc2.seek(0, 0)
    except AttributeError:
        pass

    obj1 = etree.parse(doc1)
    obj2 = etree.parse(doc2)

    buf = io.BytesIO()
    obj1.write_c14n(buf)
    buf.seek(0, 0)
    str1 = buf.read()
    str1 = [_i.strip() for _i in str1.splitlines() if _i.strip()]

    buf = io.BytesIO()
    obj2.write_c14n(buf)
    buf.seek(0, 0)
    str2 = buf.read()
    str2 = [_i.strip() for _i in str2.splitlines() if _i.strip()]

    unified_diff = difflib.unified_diff(str1, str2)

    err_msg = "\n".join(unified_diff)
    if err_msg:
        msg = "Strings are not equal.\n"
        raise AssertionError(msg + err_msg)


class ProvXMLTestCase(unittest.TestCase):
    def test_serialization_example_6(self):
        """
        Test the serialization of example 6 which is a simple entity
        description.
        """
        document = prov.ProvDocument()
        document.add_namespace(*EX_NS)
        document.add_namespace(*EX_TR)

        document.entity("tr:WD-prov-dm-20111215", (
            (prov.PROV_TYPE, prov.Literal("document", prov.XSD_QNAME)),
            ("ex:version", "2")
        ))

        with io.BytesIO() as actual:
            document.serialize(format='xml', destination=actual)
            compare_xml(os.path.join(DATA_PATH, "example_06.xml"), actual)

    def test_serialization_example_7(self):
        """
        Test the serialization of example 7 which is a basic activity.
        """
        document = prov.ProvDocument()
        document.add_namespace(*EX_NS)

        document.activity(
            "ex:a1",
            "2011-11-16T16:05:00",
            "2011-11-16T16:06:00", [
            (prov.PROV_TYPE, prov.Literal("ex:edit", prov.XSD_QNAME)),
            ("ex:host", "server.example.org")])

        with io.BytesIO() as actual:
            document.serialize(format='xml', destination=actual)
            compare_xml(os.path.join(DATA_PATH, "example_07.xml"), actual)

    def test_deserialization_example_6(self):
        """
        Test the deserialization of example 6 which is a simple entity
        description.
        """
        actual_doc = prov.ProvDocument.deserialize(
            source=os.path.join(DATA_PATH, "example_06.xml"),
            format="xml")

        expected_document = prov.ProvDocument()
        expected_document.add_namespace(*EX_NS)
        expected_document.add_namespace(*EX_TR)

        expected_document.entity("tr:WD-prov-dm-20111215", (
            (prov.PROV_TYPE, prov.Literal("document", prov.XSD_QNAME)),
            ("ex:version", "2")
        ))

        self.assertEqual(actual_doc, expected_document)

    def test_deserialization_example_7(self):
        """
        Test the deserialization of example 7 which is a simple activity
        description.
        """
        actual_doc = prov.ProvDocument.deserialize(
            source=os.path.join(DATA_PATH, "example_07.xml"),
            format="xml")

        expected_document = prov.ProvDocument()
        expected_document.add_namespace(*EX_NS)

        expected_document.activity(
            "ex:a1",
            "2011-11-16T16:05:00",
            "2011-11-16T16:06:00", [
                (prov.PROV_TYPE, prov.Literal("ex:edit", prov.XSD_QNAME)),
                ("ex:host", "server.example.org")])

        self.assertEqual(actual_doc, expected_document)


class ProvXMLRoundTripFromFileTestCase(unittest.TestCase):
    def _perform_round_trip(self, filename):
        document = prov.ProvDocument.deserialize(source=filename, format="xml")

        with io.BytesIO() as new_xml:
            document.serialize(format='xml', destination=new_xml)
            compare_xml(filename, new_xml)


# Add one test for each found file. Lazy way to do metaprogramming...
# I think parametrized tests are justified in this case as the test
# function names make it clear what is going on.
for filename in glob.iglob(os.path.join(
        DATA_PATH, "*" + os.path.extsep + "xml")):
    name = os.path.splitext(os.path.basename(filename))[0]
    test_name = "test_roundtrip_from_xml_%s" % name

    # Python creates closures on function calls...
    def get_fct(f):
        def fct(self):
            self._perform_round_trip(f)
        return fct

    fct = get_fct(filename)
    fct.__name__ = test_name

    setattr(ProvXMLRoundTripFromFileTestCase, test_name, fct)


if __name__ == '__main__':
    unittest.main()