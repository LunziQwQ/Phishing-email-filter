import os

from checker.check_status import WAITING, SAFE, THREATENING
from data.file_type_db import FileTypeDB


class AttachedChecker:
    file_type_db = None

    check_time = {
        "unusual_size": 0.1,
        "trick_type": 0.2
    }

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.is_connected = is_connected
        self.invoker = {
            "unusual_size": self.unusual_size,
            "trick_type": self.is_trick_type
        }

    def check(self, check_list):
        check_result = {
            "attached": {
                "count": len(self.eml_info.files),
                "unusual_size": {"count": 0, "status": WAITING, "process": 0},
                "trick_type": {"count": 0, "status": WAITING, "process": 0}
            }
        }
        for item in check_list:
            if item not in check_result["attached"]:
                continue

            check_result["attached"][item]["status"] = SAFE
            for file_path in self.eml_info.files:
                check_result["attached"][item]["process"] += 1
                check_result["attached"][item]["count"] += 1 if self.invoker[item](file_path) else 0
                if check_result["attached"][item]["count"] > 1:
                    check_result["attached"][item]["status"] = THREATENING
                yield check_result

    def detect_time(self, check_list):
        time = 0.0
        attach_count = len(self.eml_info.files)
        for ct in self.check_time:
            if ct in check_list:
                time += attach_count * self.check_time[ct]
        return time

    def step_count(self, check_list):
        return len(self.eml_info.files) * len(set(check_list).intersection(set(self.check_time.keys())))

    @classmethod
    def init_file_type_db(cls):
        if not cls.file_type_db:
            cls.file_type_db = FileTypeDB()

    @classmethod
    def is_trick_type(cls, file):
        cls.init_file_type_db()
        return cls.file_type_db.is_trick_type(file)

    @staticmethod
    def unusual_size(file):
        size = os.path.getsize(file) / float(1024 * 1024)  # MB
        return size > 10
