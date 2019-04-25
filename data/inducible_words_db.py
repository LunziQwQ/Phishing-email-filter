import json


class InducibleWordsDB:

    def __init__(self):
        with open("inducible_words.json", "r") as f:
            self.datas = json.load(f)

    def inducible_words(self, content, is_html=False):
        check_content = content.lower()
        count = 0

        datas = self.datas["common"]
        if is_html:
            datas += self.datas["html"]

        for inducible_word in datas:
            if inducible_word in check_content:
                count += 1

        return count
