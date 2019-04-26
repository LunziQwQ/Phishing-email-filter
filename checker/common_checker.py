from data.inducible_words_db import InducibleWordsDB

full_check_list = [
    "abnormal_time",
    "inducible_title",
    "inducible_comment"
]


class CommonChecker:
    inducible_db = None

    def __init__(self, eml_info, check_list, is_connected):
        self.eml_info = eml_info
        self.check_result = {
            "common": {
                "count": len(self.eml_info.html_block),
                "abnormal_time": 0,
                "inducible_title": 0
            }
        }
        self.check_list = check_list
        self.is_connected = is_connected

    def check(self):
        if "abnormal_time" in self.check_list:
            self.check_result["common"]["abnormal_time"] += CommonChecker.is_abnormal_time(self.eml_info)
        if "inducible_title" in self.check_list:
            self.check_result["common"]["inducible_title"] += CommonChecker.inducible_title(self.eml_info)
        if "inducible_comment" in self.check_list:
            self.check_result["common"]["inducible_comment"] += CommonChecker.inducible_comment(self.eml_info)

        return self.check_result

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
