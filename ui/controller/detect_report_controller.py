from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from checker.checker_items import full_check_items
from ui.view.DetectReport import Ui_Dialog


class DetectReportController(QMainWindow, Ui_Dialog):
    def __init__(self, email_info_list, check_list):
        super(DetectReportController, self).__init__()
        self.setupUi(self)
        self.email_info_list = email_info_list
        self.check_list = check_list

    def exec(self):
        QApplication.processEvents()
        result = {}
        for ei in self.email_info_list:
            email_info = self.email_info_list[ei]
            checker = email_info["checker"]
            for items in checker.check(self.check_list):
                for item in items:
                    result.update(item)
                    table = self.report_to_table(result)
                    email_info["table"] = table
                    self.draw_table(table)
                    QApplication.processEvents()

    @staticmethod
    def report_to_table(result):
        table = {item: [] for item in full_check_items}
        for type_items in result:
            items_count = result[type_items]["count"]
            for item in result[type_items]:
                if item == "count":
                    continue
                if result[type_items][item]["process"] == "NA":
                    safe = "NA"
                    dangerous = result[type_items][item]["count"]
                    undetected = "NA"
                    count = "NA"
                    status = result[type_items][item]["status"]
                else:
                    _done = result[type_items][item]["process"]
                    count = items_count
                    dangerous = result[type_items][item]["count"]
                    undetected = count - _done
                    safe = _done - dangerous
                    status = result[type_items][item]["status"]
                table[item] = [safe, dangerous, undetected, count, status]

        return table

    def draw_table(self, table):
        for now_row, item in enumerate(table):
            for ti, data in enumerate(table[item]):
                self.current_feedback_tableWidget.setItem(now_row, ti, QTableWidgetItem(str(data)))