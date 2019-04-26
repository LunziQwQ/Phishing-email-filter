import time

from PyQt5.QtCore import QFile, QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, QCheckBox

from checker import checker_items
from checker.checker import Checker
from reader.eml_reader import EmlReader
from ui.view.main import Ui_MainWindow
from utils.system_info import is_connected


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # set table prop
        self.email_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.email_list_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # bind sign
        self.import_btn.clicked.connect(self.import_btn_on_click)
        self.check_net_btn.clicked.connect(self.check_net_on_click)

        self.url_adv_cb.stateChanged.connect(self.test_item_changed)
        self.url_basic_cb.stateChanged.connect(self.test_item_changed)
        self.plain_cb.stateChanged.connect(self.test_item_changed)
        self.html_cb.stateChanged.connect(self.test_item_changed)
        self.accessory_cb.stateChanged.connect(self.test_item_changed)

        self.email_list_table.itemClicked.connect(self.update_detect_time_label())

        # save args
        self.email_info_list = {}
        self.check_list = []

    def import_btn_on_click(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "./", "Eml (*.eml)")
        # 打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
        # 如果用户主动关闭文件对话框，则返回值为空
        if fname[0]:  # 判断路径非空
            f = QFile(fname[0])  # 创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
            # open()会自动返回一个文件对象
            reader = EmlReader(fname[0])
            info = reader.read()
            now_row = self.email_list_table.rowCount()
            self.email_list_table.setRowCount(now_row + 1)

            cb = QTableWidgetItem()
            cb.setCheckState(Qt.Checked)

            self.email_list_table.setItem(now_row, 0, cb)

            self.email_info_list[str(now_row)] = {"checker": Checker(info), "info": info, "check_box": cb}

            self.email_list_table.setItem(now_row, 1, QTableWidgetItem(info.subject))
            self.email_list_table.setItem(now_row, 2, QTableWidgetItem(info.sender))
            self.email_list_table.setItem(now_row, 3, QTableWidgetItem(info.receiver))
            self.email_list_table.setItem(now_row, 4, QTableWidgetItem(time.asctime(info.date)))

            self.check_email_count += 1
            self.update_detect_time_label()

    def update_detect_time_label(self):
        t = 0.0
        for item in self.email_info_list.values():
            if item["check_box"].checkState() == Qt.Checked:
                checker = item["checker"]
                t += checker.detect_time(self.check_list)
        self.time_required_label.setText(str(t)[:7] + "s")

    def test_item_changed(self):
        self.check_list = []
        if self.plain_cb.checkState() == Qt.Checked:
            self.check_list.extend(checker_items.plain)

        if self.html_cb.checkState() == Qt.Checked:
            self.check_list.extend(checker_items.html)

        if self.accessory_cb.checkState() == Qt.Checked:
            self.check_list.extend(checker_items.accessory)

        if self.url_basic_cb.checkState() == Qt.Checked:
            self.check_list.extend(checker_items.url_basic)

        if self.url_adv_cb.checkState() == Qt.Checked:
            self.check_list.extend(checker_items.url_advance)

        self.update_detect_time_label()

    def check_net_on_click(self):
        if is_connected():
            self.network_status_label.setText("success")
            self.network_status_label.setStyleSheet(
                "color:rgb(28,206,8,255);")
        else:
            self.network_status_label.setText("failed")
            self.network_status_label.setStyleSheet(
                "color:rgb(200,17,17,255);")
