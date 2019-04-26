full_check_list = [
    "have_script",
]

check_time = {
    "have_script": 0.5
}


class HtmlChecker:

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.check_result = {
            "html": {
                "count": len(self.eml_info.html_block),
                "have_script": 0,
            }
        }
        self.is_connected = is_connected

    def check(self, check_list):
        for html_block in self.eml_info.html_block:
            if "have_script" in check_list:
                self.check_result["html"]["have_script"] += 1 if HtmlChecker.have_script(html_block) else 0
        return self.check_result

    def detect_time(self, check_list):
        time = 0.0
        html_count = len(self.eml_info.html_block)
        for ct in check_time:
            if ct in check_list:
                time += html_count * check_time[ct]
        return time

    @staticmethod
    def have_script(html):
        return "<script>" in html
