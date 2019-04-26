from checker.common_checker import CommonChecker
from checker.html_checker import HtmlChecker
from checker.url_checker import UrlChecker
from utils.system_info import is_connected


class Checker(object):
    detect_time = {
        "plain": 2,
        "url_basic": 0.3,
        "html": 0.2,
        "accessory": 0.1,
        "url_advance": 2
    }

    def __init__(self, email_info, check_list):
        is_online = is_connected()

        self.checkers = [
            UrlChecker(email_info, check_list, is_online),
            CommonChecker(email_info, check_list, is_online),
            HtmlChecker(email_info, check_list, is_online)
        ]

    def detect_time(self):
        time = 0.0

        for checker in self.checkers:
            time += checker.detect_time()

        return time

    def check(self):
        result = {}

        for checker in self.checkers:
            result.update(checker.check())

        return result
