import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.controller.main_controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainController()
    md.show()
    sys.exit(app.exec_())
