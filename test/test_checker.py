from unittest import TestCase
from checker.checker import Checker
from checker.checker_items import full_check_items
from reader.eml_reader import EmlReader


class TestChecker(TestCase):
    def test_check(self):
        eml_file = "test.eml"
        reader = EmlReader(eml_file)
        info = reader.read()
        report = Checker(info).check(full_check_items)
        print(report)