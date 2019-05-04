import json
import os


class FileTypeDB:

    def __init__(self):
        with open("data/file_type_data.json", "r", encoding="utf-8") as f:
            self.datas = json.loads(f.read())

    def is_trick_type(self, file):
        with open(file, "rb") as f:
            bs = f.read(20)
        prefix = ""
        _, ext = os.path.splitext(file)
        for b in bs:
            t = b & 0xFF
            prefix += '{:02x}'.format(t)
        for pre in self.datas:
            if prefix.startswith(pre):
                return ext.replace(".", "") not in self.datas[pre]
        return False
