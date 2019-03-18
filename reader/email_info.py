import email
import os
import time
import re
from os import path


class EmailInfo:

    def __init__(self, eml):
        self.is_multipart = eml.is_multipart()
        self.subject = eml.get("subject")
        self.sender = email.utils.parseaddr(eml.get("from"))[1]
        self.receiver = email.utils.parseaddr(eml.get("to"))[1]
        self.date = email.utils.parsedate(eml.get("date"))
        self.mime_version = eml.get("MIME_Version")
        self.content_type = eml.get_content_type()
        self.boundary = eml.get_boundary()
        self.html_block = []
        self.plain_block = []
        self.files = []

        if eml.is_multipart():
            for block in eml.walk():
                if block.get_content_type() == "text/html":
                    self.html_block.append(block.get_payload(decode=True).decode())
                if block.get_content_type() == "text/plain":
                    self.plain_block.append(block.get_payload(decode=True).decode())
                if block.get_filename():
                    file_name = block.get_filename()
                    file_data = block.get_payload(decode=True)
                    save_path = path.join("/tmp/pef/pef_files", self.subject, file_name)
                    if not path.exists(path.dirname(save_path)):
                        os.makedirs(path.dirname(save_path))

                    with open(path.join("/tmp/pef/pef_files", self.subject, file_name), "wb") as f:
                        f.write(file_data)
                    self.files.append(save_path)
        self.links = self.get_links()

    def get_links(self):
        links = []
        for html in self.html_block:
            links.extend(re.findall("""<a[^>]+?href=["']?([^"']+)["']?[^>]*>([^<]+)</a>""", html))

        return links

    def __str__(self):
        return "====== eml info ======\n" \
               "subject: %s\n" \
               "sender: %s\n" \
               "receiver: %s\n" \
               "date: %s\n" \
               "is_multipart: %s\n" \
               "mime_version: %s\n" \
               "content_type: %s\n" \
               "boundary: %s\n" \
               "html_block: %s\n" \
               "plain_block: %s\n" \
               "files: %s\n" \
               "======================\n" % (
                   self.subject, self.sender, self.receiver, time.asctime(self.date), self.is_multipart,
                   self.mime_version,
                   self.content_type, self.boundary,
                   len(self.html_block),
                   len(self.plain_block),
                   len(self.files))
