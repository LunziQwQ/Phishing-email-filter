import httplib2
import urllib3
import json
import datetime

api_url = """http://api.whoapi.com/?apikey=cdb3d16c31c7265968b69ab5e3ed25ca&r=whois&domain="""


def get_create_time(url):
    conn = httplib2.HTTPConnectionWithTimeout("api.whoapi.com")
    parse_result = urllib3.util.parse_url(url)
    query_url = api_url + parse_result.netloc

    conn.request("GET", query_url)
    info = json.loads(conn.getresponse().read())
    if info["status"] != '0':
        return None
    else:
        create_time = info.get("date_created", None)
        return datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M:%S') if create_time else None
