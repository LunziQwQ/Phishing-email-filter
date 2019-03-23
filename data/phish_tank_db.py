import json


class PhishTankDB:

    def __init__(self):
        with open("phish_urls.json", "r") as f:
            self.datas = json.load(f)

    def is_phish_url(self, url):
        for phish_url in self.datas:
            if url.startswith(phish_url):
                return True

        return False
