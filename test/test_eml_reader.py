from unittest import TestCase
from reader.eml_reader import EmlReader


class TestEmlReader(TestCase):
    def test_read(self):
        eml_file = "test.eml"
        reader = EmlReader(eml_file)
        info = reader.read()
        print(info)
        self.assertIsNotNone(reader)
        self.assertIsNotNone(info)
