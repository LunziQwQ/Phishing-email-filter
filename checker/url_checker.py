import datetime
import urllib3
import re

from data.phish_tank_db import PhishTankDB
from data.unusual_char_db import UnusualCharDB
from utils.sogou_rank_query import get_sogou_rank
from utils.whois_query import get_create_time

ip_regex = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
full_check_list = [
    "have_ip",
    "netloc_too_long",
    "low_pr",
    "have_unusual",
    "in_phish_tank",
    "create_less_3_month",
    "have_redirect"
]


class UrlChecker:
    phish_tank_db = None
    unusual_db = None

    def __init__(self, eml_info, check_list, is_connected):
        self.eml_info = eml_info
        self.check_result = {
            "url": {
                "count": len(self.eml_info.urls),
                "have_ip": 0,
                "netloc_too_long": 0,
                "low_pr": 0,
                "have_unusual": 0,
                "in_phish_tank": 0,
                "create_less_3_month": 0,
                "redirect": 0
            }
        }
        self.check_list = check_list
        self.is_connected = is_connected

    def check(self):
        for url in self.eml_info.urls:
            if "have_ip" in self.check_list:
                self.check_result["url"]["have_ip"] += 1 if UrlChecker.have_ip(url) else 0
            if "netloc_too_long" in self.check_list:
                self.check_result["url"]["netloc_too_long"] += 1 if UrlChecker.netloc_too_long(url) else 0
            if "have_unusual" in self.check_list:
                self.check_result["url"]["have_unusual"] += 1 if UrlChecker.have_unusual_char(url) else 0
            if "in_phish_tank" in self.check_list:
                self.check_result["url"]["in_phish_tank"] += 1 if UrlChecker.in_phish_tank(url) else 0

            if self.is_connected:

                if "create_less_3_month" in self.check_list:
                    self.check_result["url"]["create_less_3_month"] += 1 if UrlChecker.create_less_3_month(url) else 0
                if "low_pr" in self.check_list:
                    self.check_result["url"]["low_pr"] += 1 if UrlChecker.low_pr(url) else 0

        return self.check_result

    @classmethod
    def init_phish_tank_db(cls):
        cls.phish_tank_db = PhishTankDB()

    @classmethod
    def init_unusual_db(cls):
        cls.unusual_db = UnusualCharDB()

    @staticmethod
    def have_ip(url):
        return len(re.findall(ip_regex, url)) > 0

    @staticmethod
    def netloc_too_long(url):
        return len(urllib3.util.parse_url(url).netloc) > 30

    @staticmethod
    def have_redirect(url):
        return "&redirect" in url.lower()

    @staticmethod
    def low_pr(url):
        if get_sogou_rank(url) < 3:
            return True
        return False

    @classmethod
    def in_phish_tank(cls, url):
        if not cls.phish_tank_db:
            cls.init_phish_tank_db()

        return cls.phish_tank_db.is_phish_url(url)

    @classmethod
    def have_unusual_char(cls, url):
        if not cls.unusual_db:
            cls.init_unusual_db()
        return cls.unusual_db.have_unusual(url)

    @staticmethod
    def create_less_3_month(url):
        create_time = get_create_time(url)
        if create_time is None:
            return False
        else:
            return (datetime.datetime.now() - create_time).days < 90
