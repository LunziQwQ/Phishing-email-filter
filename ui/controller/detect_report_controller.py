import copy

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from checker.checker_items import full_check_items
from evaluation.evaluation import Evaluation
from ui.view.DetectReport import Ui_Dialog


class DetectReportController(QMainWindow, Ui_Dialog):
    def __init__(self, email_info_list, check_list):
        super(DetectReportController, self).__init__()
        self.setupUi(self)
        self.email_info_list = email_info_list
        self.check_list = copy.deepcopy(check_list)

        self.total_feedback_tableWidget.cellClicked.connect(self.email_list_table_on_click)
        self.total_feedback_tableWidget.focusOutEvent = self.email_list_table_out_focus

        self.update_feedback = True
        self.total_progressBar.setValue(0)
        self.process_value = 0.0

        step_count = 0
        for info_index in self.email_info_list:
            step_count += self.email_info_list[info_index]["checker"].step_count(self.check_list)
        self.step_length = 100.0 / step_count if step_count != 0 else 1

        self.email_list_table = [[self.email_info_list[info_index]["info"].subject, "waiting", "", ""] for info_index in
                                 email_info_list]
        self.draw_email_list_table()

    def update_process(self, add):
        self.process_value += add
        if self.process_value > 100:
            self.process_value = 100
        self.total_progressBar.setValue(self.process_value)

    def exec(self):
        QApplication.processEvents()
        result = {}
        for ei, eml_info in enumerate(self.email_info_list):
            email_info = self.email_info_list[eml_info]
            checker = email_info["checker"]
            self.current_email_subject_label.setText(email_info["info"].subject)
            self.email_list_table[ei][1] = "processing"
            self.draw_email_list_table()
            for items in checker.check(self.check_list):
                for item in items:
                    result.update(item)

                    table = self.report_to_feedback_table(result)
                    email_info["table"] = table

                    self.update_process(self.step_length)
                    self.draw_feedback_table(table)

                    score = Evaluation.evaluate(result)
                    self.email_list_table[ei][2] = "safe" if score < 35 else "threatening"
                    self.email_list_table[ei][3] = "%.2f%%" % score
                    self.draw_email_list_table()

                    QApplication.processEvents()
            self.email_list_table[ei][1] = "finished"
            self.draw_email_list_table()

        self.total_progressBar.setValue(100)
        QMessageBox.information(self, "Check Finish", "Check all email finish!~", QMessageBox.Yes)

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

    def draw_feedback_table(self, table, force_update=False):
        if self.update_feedback or force_update:
            for now_row, item in enumerate(table):
                if item in self.check_list:
                    for ti, data in enumerate(table[item]):
                        self.current_feedback_tableWidget.setItem(now_row, ti, QTableWidgetItem(str(data)))

    def draw_email_list_table(self):
        for now_row, eml in enumerate(self.email_list_table):
            self.total_feedback_tableWidget.setRowCount(now_row + 1)
            for ti, data in enumerate(eml):
                self.total_feedback_tableWidget.setItem(now_row, ti, QTableWidgetItem(str(data)))

    def email_list_table_on_click(self, row, column):
        self.update_feedback = self.email_list_table[row][1] == "processing"
        if "table" in self.email_info_list[str(row)]:
            self.current_email_subject_label.setText(self.email_info_list[str(row)]["info"].subject)
            self.draw_feedback_table(self.email_info_list[str(row)]["table"], force_update=True)
            QApplication.processEvents()

    def email_list_table_out_focus(self, event):
        self.update_feedback = True
