from checker.url_checker import UrlChecker


def check(email_info):
    result = {
        "url": {
            "count": 0,
            "have_ip": 0
        }
    }

    # check url
    for link in email_info.links:

        # check url have ip
        if UrlChecker.have_ip(link):
            result["url"]["have_ip"] += 1

    return result
