import time
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtWidgets

from ui.view.Congratulation import Ui_Dialog


class CongratulationController(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(CongratulationController, self).__init__()
        self.setupUi(self)
        self.update_completed_label.setText("Updating. Pleast wait")
        self.ok_btn.clicked.connect(self.close)

    def start_update(self):
        time.sleep(random.randint(0, 8))
        self.update_completed_label.setText("Update Completed~")
