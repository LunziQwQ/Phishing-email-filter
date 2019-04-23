from unittest import TestCase
from checker.url_checker import UrlChecker, full_check_list
from reader.eml_reader import EmlReader
from utils.system_info import is_connected


class TestUrlChecker(TestCase):
    def test_check(self):
        eml_file = "test.eml"
        info = EmlReader(eml_file).read()
        is_online = is_connected()
        checker = UrlChecker(info, full_check_list, is_online)
        result = checker.check()
        self.assertEqual(result["url"]["netloc_too_long"], 0)
        self.assertEqual(result["url"]["low_pr"], 4)
