import logging
import unittest

from prov.model import ProvDocument

try:
    from cStringIO import StringIO
    assert StringIO
except ImportError:
    from StringIO import StringIO
    assert StringIO


logger = logging.getLogger(__name__)


class BaseRoundTripTest(unittest.TestCase):
    def setUp(self):
        # a dictionary to hold test documents
        self._documents = dict()

    def write(self, document, fp):
        pass

    def read(self, fp):
        return None

    def compare_documents(self, doc_1, doc_2):
        # Self equality check
        self.assertEqual(doc_1, doc_1)
        self.assertEqual(doc_2, doc_2)
        # Equality check
        try:
            self.assertEqual(doc_1, doc_2)
        except AssertionError, e:
            logger.info(u'---- Document 1 ----\n' + doc_1.get_provn())
            logger.info(u'---- Document 2 ----\n' + doc_2.get_provn())
            # Re-raise the exception
            raise e

    def run_roundtrip_test_document(self, document):
        stream = StringIO()
        self.write(document, stream)
        stream.seek(0)
        doc_2 = self.read(stream)
        self.compare_documents(document, doc_2)


class ProvJSONRoundTripTest(BaseRoundTripTest):
    def write(self, document, fp):
        document.serialize(fp)

    def read(self, fp):
        return ProvDocument.deserialize(fp)

