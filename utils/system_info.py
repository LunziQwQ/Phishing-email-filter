def is_connected():
    import requests
    try:
        _ = requests.get("http://www.taobao.com", timeout=5)
    except Exception as _:
        return False
    return True
