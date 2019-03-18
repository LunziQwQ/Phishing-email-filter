from unittest import TestCase
from reader.eml_reader import EmlReader


class TestEmailInfo(TestCase):
    def test_get_links(self):
        eml_file = "test.eml"
        info = EmlReader(eml_file).read()
        self.assertEqual(len(info.get_links()), 4)
