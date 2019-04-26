import email
import os
import time
import re
from os import path


class EmailInfo:
    def __init__(self, eml):
        """
        构造方法，从eml对象中解析出数据
        :param eml: eml_reader获取的eml对象
        """
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

                try:
                    # 保存html类型的内容块
                    if block.get_content_type() == "text/html":
                        self.html_block.append(block.get_payload(decode=True).strip().decode())

                    # 保存plain文本的内容块
                    if block.get_content_type() == "text/plain":
                        self.plain_block.append(block.get_payload(decode=True).strip().decode())
                except UnicodeDecodeError:
                    # 适应中文编码
                    if block.get_content_type() == "text/html":
                        self.html_block.append(block.get_payload(decode=True).strip().decode("gbk"))

                    # 适应中文编码
                    if block.get_content_type() == "text/plain":
                        self.plain_block.append(block.get_payload(decode=True).strip().decode("gbk"))

                # 保存附件到/tmp/pef/pef_files
                if block.get_filename():
                    file_name = block.get_filename()
                    file_data = block.get_payload(decode=True)
                    save_path = path.join("/tmp/pef/pef_files", self.subject, file_name)
                    if not path.exists(path.dirname(save_path)):
                        os.makedirs(path.dirname(save_path))

                    with open(path.join("/tmp/pef/pef_files", self.subject, file_name), "wb") as f:
                        f.write(file_data)
                    self.files.append(save_path)

        self.a_tags = self.get_a_tags()
        self.urls = [a_tag[0] for a_tag in self.a_tags]

    def get_a_tags(self):
        """
        通过正则表达式，匹配所有html块里的a标签内容
        :return: 元组列表 -> (url, 描述文字)
        """
        links = []
        for html in self.html_block:
            links.extend(re.findall("""<a[^>]+?href=["']?([^"']+)["']?[^>]*>([^<]+)</a>""", html))

        return links

    def __str__(self):
        """
        将对象转化为字符串，在输出时会默认调用
        :return: string
        """

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
