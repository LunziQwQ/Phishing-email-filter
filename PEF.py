#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from ui.controller.main_controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainController()
    md.show()
    sys.exit(app.exec_())
