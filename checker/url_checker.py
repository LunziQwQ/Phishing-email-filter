from checker.sogou_rank_query import get_sogou_rank


class UrlChecker:
    @staticmethod
    def have_ip(url):
        # TODO
        return False

    @staticmethod
    def too_long(url):
        # TODO
        return False

    @staticmethod
    def low_pr(url):
        if get_sogou_rank(url) < 3:
            return True
        return False
