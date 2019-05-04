import datetime
import urllib3
import re

from data.phish_tank_db import PhishTankDB
from data.unusual_char_db import UnusualCharDB
from utils.sogou_rank_query import get_sogou_rank
from utils.whois_query import get_create_time
from checker.check_status import WAITING, SAFE, THREATENING


class UrlChecker:
    phish_tank_db = None
    unusual_db = None

    ip_regex = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'

    check_time = {
        "have_ip": 0.02,
        "netloc_too_long": 0.02,
        "low_pr": 1.5,
        "have_unusual": 0.02,
        "in_phish_tank": 0.5,
        "create_less_3_month": 1.7,
        "have_redirect": 0.02
    }

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.is_connected = is_connected

        self.invoker = {
            "have_ip": UrlChecker.have_ip,
            "netloc_too_long": UrlChecker.netloc_too_long,
            "low_pr": UrlChecker.low_pr,
            "have_unusual": UrlChecker.have_unusual_char,
            "in_phish_tank": UrlChecker.in_phish_tank,
            "create_less_3_month": UrlChecker.create_less_3_month,
            "have_redirect": UrlChecker.have_redirect
        }

    def check(self, check_list):
        check_result = {
            "url": {
                "count": len(self.eml_info.urls),
                "have_ip": {"count": 0, "status": WAITING, "process": 0},
                "netloc_too_long": {"count": 0, "status": WAITING, "process": 0},
                "low_pr": {"count": 0, "status": WAITING, "process": 0},
                "have_unusual": {"count": 0, "status": WAITING, "process": 0},
                "in_phish_tank": {"count": 0, "status": WAITING, "process": 0},
                "create_less_3_month": {"count": 0, "status": WAITING, "process": 0},
                "have_redirect": {"count": 0, "status": WAITING, "process": 0}
            }
        }

        if not self.is_connected:
            if "create_less_3_month" in check_list:
                check_list.remove("create_less_3_month")
            if "low_pr" in check_list:
                check_list.remove("low_pr")

        for item in check_list:
            if item not in check_result["url"]:
                continue

            check_result["url"][item]["status"] = SAFE
            for url in self.eml_info.urls:
                check_result["url"][item]["process"] += 1
                check_result["url"][item]["count"] += 1 if self.invoker[item](url) else 0
                if check_result["url"][item]["count"] > 1:
                    check_result["url"][item]["status"] = THREATENING
                yield check_result

            if len(self.eml_info.urls) == 0:
                yield check_result

    def detect_time(self, check_list):
        time = 0.0
        url_count = len(self.eml_info.urls)
        for ct in self.check_time:
            if ct in check_list:
                time += url_count * self.check_time[ct]
        return time

    def step_count(self, check_list):
        return len(self.eml_info.urls) * len(set(check_list).intersection(set(self.check_time.keys())))

    @classmethod
    def init_phish_tank_db(cls):
        if not cls.phish_tank_db:
            cls.phish_tank_db = PhishTankDB()

    @classmethod
    def init_unusual_db(cls):
        if not cls.unusual_db:
            cls.unusual_db = UnusualCharDB()

    @classmethod
    def have_ip(cls, url):
        return len(re.findall(cls.ip_regex, url)) > 0

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
        cls.init_phish_tank_db()
        return cls.phish_tank_db.is_phish_url(url)

    @classmethod
    def have_unusual_char(cls, url):
        cls.init_unusual_db()
        return cls.unusual_db.have_unusual(url)

    @staticmethod
    def create_less_3_month(url):
        create_time = get_create_time(url)
        if create_time is None:
            return False
        else:
            return (datetime.datetime.now() - create_time).days < 90
