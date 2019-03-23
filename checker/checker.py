from checker.url_checker import UrlChecker
from utils.system_info import is_connected
from data.phish_tank_db import PhishTankDB
from data.unusual_char_db import UnusualCharDB


class Checker(object):

    def __init__(self):
        self.phish_tank_db = None
        self.unusual_db = None

    def init_phish_tank_db(self):
        self.phish_tank_db = PhishTankDB()

    def init_unusual_db(self):
        self.unusual_db = UnusualCharDB()

    def check(self, email_info):
        result = {
            "url": {
                "count": len(email_info.links),
                "have_ip": 0,
                "netloc_too_long": 0,
                "low_pr": 0,
                "have_unusual": 0,
                "in_phish_tank": 0
            }
        }

        # check url
        for link in email_info.links:

            # 检查链接中包含IP
            if UrlChecker.have_ip(link):
                result["url"]["have_ip"] += 1

            # 检查链接主域名过长
            if UrlChecker.netloc_too_long(link):
                result["url"]["netloc_too_long"] += 1

            # 检查是否存在特殊字符
            if self.unusual_db and UrlChecker.have_unusual_char(link, self.unusual_db):
                result["url"]["have_unusual"] += 1

            # 检查是否存在于PhishTank数据库
            if self.phish_tank_db and UrlChecker.in_phish_tank(link, self.phish_tank_db):
                result["url"]["in_phish_tank"] += 1

            # 依赖网络接口的检查
            if is_connected():

                # 检查PageRank过低
                if UrlChecker.low_pr(link):
                    result["url"]["low_pr"] += 1

        return result
