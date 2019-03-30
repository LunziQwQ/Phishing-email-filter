from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.main import Ui_MainWindow


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
