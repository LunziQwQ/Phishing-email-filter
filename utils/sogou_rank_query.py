import httplib2
import urllib3

api_url = """http://www.sogou.com/sogourank?ur="""


def get_sogou_rank(url):
    conn = httplib2.HTTPConnectionWithTimeout("www.sogou.com")
    parse_result = urllib3.util.parse_url(url)
    query_url = api_url + parse_result.scheme + "://" + parse_result.netloc + "/"

    conn.request("GET", query_url)
    resp = conn.getresponse()
    return int(resp.read()[10:11])
