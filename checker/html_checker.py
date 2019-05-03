from checker.check_status import WAITING, SAFE, THREATENING


class HtmlChecker:
    check_time = {
        "have_script": 0.5
    }

    def __init__(self, eml_info, is_connected):
        self.eml_info = eml_info
        self.is_connected = is_connected
        self.invoker = {
            "have_script": self.have_script
        }

    def check(self, check_list):
        check_result = {
            "html": {
                "count": len(self.eml_info.html_block),
                "have_script": {"count": 0, "status": WAITING, "process": 0}
            }
        }
        for item in check_list:
            if item not in check_result["html"]:
                continue

            check_result["html"][item]["status"] = SAFE
            for html_block in self.eml_info.html_block:
                check_result["html"][item]["process"] += 1
                check_result["html"][item]["count"] += 1 if self.invoker[item](html_block) else 0
                if check_result["html"][item]["count"] > 1:
                    check_result["html"][item]["status"] = THREATENING
                yield check_result

    def detect_time(self, check_list):
        time = 0.0
        html_count = len(self.eml_info.html_block)
        for ct in self.check_time:
            if ct in check_list:
                time += html_count * self.check_time[ct]
        return time

    def step_count(self, check_list):
        return len(self.eml_info.html_block) * len(set(check_list).intersection(set(self.check_time.keys())))

    @staticmethod
    def have_script(html):
        return "<script>" in html or "</script>"
