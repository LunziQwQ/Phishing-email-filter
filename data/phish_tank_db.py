import json


class PhishTankDB:

    def __init__(self):
        with open("online-valild.json", "r") as f:
            self.datas = json.load(f)

    def is_phish_url(self, url):
        for item in self.datas:
            if url.startswith(item["url"]):
                return True

        return False
