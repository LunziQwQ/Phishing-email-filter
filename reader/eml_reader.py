import email
import os


class Reader:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError

        with open(path, "r") as f:
            self.eml = email.message_from_file(f)

    def read(self):
        info = EmailInfo()
        return info


class EmailInfo:
    def __init__(self):
        pass


def read_eml(path):
    reader = Reader(path)
    return reader.read()
