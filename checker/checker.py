from checker.url_checker import UrlChecker
from utils.system_info import is_connected


class Checker(object):

    def __init__(self):
        self.phish_tank_db = None
        self.unusual_db = None

    def check(self, email_info, check_list):
        is_online = is_connected()
        checkers = [
            UrlChecker(email_info, check_list, is_online),
        ]
        result = {}

        for checker in checkers:
            result.update(checker.check())

        return result
