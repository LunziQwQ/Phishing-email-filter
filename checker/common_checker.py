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
        self.invoker = {
            "abnormal_time": self.is_abnormal_time,
            "inducible_title": self.inducible_title,
            "inducible_content": self.inducible_content,
        }

    def check(self, check_list):
        check_result = {
            "common": {
                "count": 1,
                "abnormal_time": {"count": 0, "status": WAITING, "process": 0},
                "inducible_title": {"count": 0, "status": WAITING, "process": "NA"},
                "inducible_content": {"count": 0, "status": WAITING, "process": "NA"}
            }
        }
        for item in check_list:
            if item not in check_result["common"]:
                continue

            check_result["common"][item]["status"] = PROCESSING
            check_result["common"][item]["count"] += self.invoker[item](self.eml_info)
            if check_result["common"][item]["process"] != "NA":
                check_result["common"][item]["process"] += 1
            check_result["common"][item]["status"] = SAFE if \
                check_result["common"][item]["count"] else THREATENING
            yield check_result

    def detect_time(self, check_list):
        time = self.check_time["abnormal_time"] + self.check_time["inducible_title"]
        for pb in self.eml_info.plain_block:
            if "inducible_content" in check_list:
                time += len(pb) * self.check_time["inducible_content"]
        return time

    def step_count(self, check_list):
        plain_chunk_size = len(set(check_list).intersection({"inducible_title", "inducible_content"}))
        return 1 + len(self.eml_info.plain_block) * plain_chunk_size

    @classmethod
    def init_inducible_db(cls):
        if not cls.inducible_db:
            cls.inducible_db = InducibleWordsDB()

    @staticmethod
    def is_abnormal_time(eml_info):
        return 1 if eml_info.date[3] in range(0, 6) else 0

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
