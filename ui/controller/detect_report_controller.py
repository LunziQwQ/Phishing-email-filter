
from PyQt5.QtWidgets import QMainWindow

from ui.view.DetectReport import Ui_Dialog


class DetectReportController(QMainWindow, Ui_Dialog):
    def __init__(self, email_info_list, check_list):
        super(DetectReportController, self).__init__()
        self.setupUi(self)
        self.email_info_list = email_info_list
        self.check_list = check_list
