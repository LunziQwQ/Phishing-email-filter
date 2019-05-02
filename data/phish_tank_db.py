import json


class PhishTankDB:

    def __init__(self):
        with open("data/phish_urls.json", "r", encoding="utf-8") as f:
            self.datas = json.loads(f.read())

    def is_phish_url(self, url):
        for phish_url in self.datas:
            if url.startswith(phish_url):
                return True

        return False
