from unittest import TestCase
from utils.sogou_rank_query import get_sogou_rank
from utils.system_info import is_connected


class TestGetSogouRank(TestCase):
    def test_get_sogou_rank(self):
        if is_connected():
            baidu_url = "http://www.baidu.com"
            self.assertEqual(get_sogou_rank(baidu_url), 9)
        else:
            return
