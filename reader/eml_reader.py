import email
import mailbox
import os
from reader.email_info import EmailInfo


class EmlReader:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError
        self.emls = []

        _, ext = os.path.splitext(path)
        if ext == "mbox":
            for message in mailbox.mbox("/Users/lunzi/Projects/Python/phishing-email-filter/sample_emls/phishing-2015"):
                try:
                    eml = email.message_from_string(message)
                    self.emls.append(eml)
                except Exception:
                    print("parse error. skip one~")

        if ext == "eml":
            with open(path, "r") as f:
                self.emls.append(email.message_from_file(f))

    def read(self):
        return [EmailInfo(eml) for eml in self.emls]
