from data.inducible_words_db import InducibleWordsDB
from checker.check_status import WAITING, SAFE, THREATENING, PROCESSING


class CommonChecker:
    inducible_db = None

    check_time = {
        "abnormal_time": 0.01,
        "inducible_title": 0.01,
        "inducible_content": 0.0001
    }

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.is_conected = is_connected

        self.check_result = {
            "common": {
                "count": len(self.eml_info.html_block),
                "abnormal_time": {"count": 0, "status": WAITING, "process": 0},
                "inducible_title": {"count": 0, "status": WAITING, "process": "NA"},
                "inducible_content": {"count": 0, "status": WAITING, "process": "NA"}
            }
        }

        self.invoker = {
            "abnormal_time": self.is_abnormal_time,
            "inducible_title": self.inducible_title,
            "inducible_content": self.inducible_content,
        }

    def check(self, check_list):
        for item in check_list:
            if item not in self.check_result["common"]:
                continue

            self.check_result["common"][item]["status"] = PROCESSING
            self.check_result["common"][item]["count"] += self.invoker[item](self.eml_info)
            self.check_result["common"][item]["status"] = SAFE if \
                self.check_result["common"][item]["count"] else THREATENING
            yield self.check_result

    def detect_time(self, check_list):
        time = self.check_time["abnormal_time"] + self.check_time["inducible_title"]
        for pb in self.eml_info.plain_block:
            if "inducible_content" in check_list:
                time += len(pb) * self.check_time["inducible_content"]
        return time

    @classmethod
    def init_inducible_db(cls):
        if not cls.inducible_db:
            cls.inducible_db = InducibleWordsDB()

    @staticmethod
    def is_abnormal_time(eml_info):
        return eml_info.date[3] in range(0, 6)

    @classmethod
    def inducible_title(cls, eml_info):
        cls.init_inducible_db()
        return cls.inducible_db.inducible_words(content=eml_info.subject)

    @classmethod
    def inducible_content(cls, eml_info):
        cls.init_inducible_db()
        count = 0
        for pb in eml_info.plain_block:
            count += cls.inducible_db.inducible_words(content=pb)
        return count
