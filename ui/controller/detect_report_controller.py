import copy
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from checker.checker_items import full_check_items
from ui.view.DetectReport import Ui_Dialog


class DetectReportController(QMainWindow, Ui_Dialog):
    def __init__(self, email_info_list, check_list):
        super(DetectReportController, self).__init__()
        self.setupUi(self)
        self.email_info_list = email_info_list
        self.check_list = copy.deepcopy(check_list)
        self.total_progressBar.setValue(0)

        chunk_length = 0
        for ei in self.email_info_list:
            chunk_length += self.email_info_list[ei]["checker"].step_count(self.check_list)
        self.step_add = 100.0 / chunk_length if chunk_length != 0 else 0

    def update_process(self, add):
        value = self.total_progressBar.value()
        now_value = value + add
        if now_value > 100:
            now_value = 100
        self.total_progressBar.setValue(now_value)

    def exec(self):
        QApplication.processEvents()
        result = {}
        for ei in self.email_info_list:
            email_info = self.email_info_list[ei]
            checker = email_info["checker"]
            self.current_email_subject_label.setText(email_info["info"].subject)
            for items in checker.check(self.check_list):
                for item in items:
                    result.update(item)
                    table = self.report_to_feedback_table(result)
                    email_info["table"] = table
                    self.draw_feedback_table(table)
                    self.update_process(self.step_add)
                    QApplication.processEvents()
                    time.sleep(0.1)
            self.update_process(self.step_add)

        self.total_progressBar.setValue(100)

    @staticmethod
    def report_to_feedback_table(result):
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

    def draw_feedback_table(self, table):
        for now_row, item in enumerate(table):
            if item in self.check_list:
                for ti, data in enumerate(table[item]):
                    self.current_feedback_tableWidget.setItem(now_row, ti, QTableWidgetItem(str(data)))
