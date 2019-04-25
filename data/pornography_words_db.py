import base64
import json


class PornographyWordsDB:

    def __init__(self):
        with open("pornography_words.json", "r") as f:
            self.datas = [base64.b64decode(x.encode("utf-8")).decode("utf-8").lower() for x in json.load(f)]

    def pornography_words(self, content):
        check_content = content.lower()
        count = 0

        for pornography_word in self.datas:
            if pornography_word in check_content:
                count += 1

        return count
