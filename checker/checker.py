from checker.url_checker import UrlChecker
from utils.system_info import is_connected


def check(email_info):
    result = {
        "url": {
            "count": len(email_info.links),
            "have_ip": 0,
            "netloc_too_long": 0,
            "low_pr": 0
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

        # 依赖网络接口的检查
        if is_connected():

            # 检查PageRank过低
            if UrlChecker.low_pr(link):
                result["url"]["low_pr"] += 1

    return result
