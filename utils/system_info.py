import httplib2


def is_connected():
    try:
        conn = httplib2.HTTPConnectionWithTimeout("www.sogou.com", timeout=5)
        conn.request("GET", "www.sogou.com")
        resp = conn.getresponse()
    except Exception as _:
        return False
    return True
