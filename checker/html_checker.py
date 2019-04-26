full_check_list = [
    "have_script",
]


class HtmlChecker:

    def __init__(self, eml_info, check_list, is_connected):
        self.eml_info = eml_info
        self.check_result = {
            "html": {
                "count": len(self.eml_info.html_block),
                "have_script": 0,
            }
        }
        self.check_list = check_list
        self.is_connected = is_connected

    def check(self):
        for html_block in self.eml_info.html_block:
            if "have_script" in self.check_list:
                self.check_result["html"]["have_script"] += 1 if HtmlChecker.have_script(html_block) else 0
        return self.check_result

    @staticmethod
    def have_script(html):
        return "<script>" in html
