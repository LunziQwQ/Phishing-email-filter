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
        if ext == ".mbox":
            for message in mailbox.mbox(path):
                try:
                    eml = email.message_from_string(str(message))
                    self.emls.append(eml)
                except Exception as e:
                    print("parse error. skip one~")

        if ext == ".eml":
            with open(path, "r") as f:
                self.emls.append(email.message_from_file(f))

    def read(self):
        list = []
        skip = 0
        for eml in self.emls:
            try:
                info = EmailInfo(eml)
                list.append(info)
            except UnicodeDecodeError:
                skip += 1

        return list, skip, len(self.emls)
