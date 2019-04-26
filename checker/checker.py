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
