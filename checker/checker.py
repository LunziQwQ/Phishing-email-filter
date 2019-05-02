from checker.common_checker import CommonChecker
from checker.html_checker import HtmlChecker
from checker.url_checker import UrlChecker
from utils.system_info import is_connected


class Checker(object):

    def __init__(self, email_info):
        # is_online = is_connected()
        self.is_online = False

        self.checkers = [
            UrlChecker(email_info, self.is_online),
            CommonChecker(email_info, self.is_online),
            HtmlChecker(email_info, self.is_online)
        ]

    def detect_time(self, checker_list):
        time = 0.0

        for checker in self.checkers:
            time += checker.detect_time(checker_list)

        return time

    def check(self, checker_list):
        for checker in self.checkers:
            yield checker.check(checker_list)
