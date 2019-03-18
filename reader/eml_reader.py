import email
import os
from reader.email_info import EmailInfo


class EmlReader:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError

        with open(path, "r") as f:
            self.eml = email.message_from_file(f)

    def read(self):
        info = EmailInfo(self.eml)
        return info
