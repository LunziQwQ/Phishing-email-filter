from data.inducible_words_db import InducibleWordsDB

full_check_list = [
    "abnormal_time",
    "inducible_title",
    "inducible_comment"
]

check_time = {
    "abnormal_time": 0.01,
    "inducible_title": 0.01,
    "inducible_comment": 0.0001
}


class CommonChecker:
    inducible_db = None

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.check_result = {
            "common": {
                "count": len(self.eml_info.html_block),
                "abnormal_time": 0,
                "inducible_title": 0,
                "inducible_comment": 0
            }
        }
        self.is_connected = is_connected

    def check(self, check_list):
        if "abnormal_time" in check_list:
            self.check_result["common"]["abnormal_time"] += CommonChecker.is_abnormal_time(self.eml_info)
        if "inducible_title" in check_list:
            self.check_result["common"]["inducible_title"] += CommonChecker.inducible_title(self.eml_info)
        if "inducible_content" in check_list:
            self.check_result["common"]["inducible_comment"] += CommonChecker.inducible_comment(self.eml_info)

        return self.check_result

    def detect_time(self, check_list):
        time = check_time["abnormal_time"] + check_time["inducible_title"]
        for pb in self.eml_info.plain_block:
            if "inducible_comment" in check_list:
                time += len(pb) * check_time["inducible_comment"]
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
    def inducible_comment(cls, eml_info):
        cls.init_inducible_db()
        count = 0
        for pb in eml_info.plain_block:
            count += cls.inducible_db.inducible_words(content=pb)
        return count
