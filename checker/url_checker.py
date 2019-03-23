import datetime
import urllib3
import re

from utils.sogou_rank_query import get_sogou_rank
from utils.whois_query import get_create_time

ip_regex = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'


class UrlChecker:
    @staticmethod
    def have_ip(url):
        return len(re.findall(ip_regex, url)) > 0

    @staticmethod
    def netloc_too_long(url):
        return len(urllib3.util.parse_url(url).netloc) > 24

    @staticmethod
    def low_pr(url):
        if get_sogou_rank(url) < 3:
            return True
        return False

    @staticmethod
    def in_phish_tank(url, db):
        return db.is_phish_url(url)

    @staticmethod
    def have_unusual_char(url, db):
        return db.have_unusual(url)

    @staticmethod
    def create_less_3_month(url):
        create_time = get_create_time(url)
        if create_time is None:
            return False
        else:
            return (datetime.datetime.now() - create_time).days < 90
