from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from reader.eml_reader import EmlReader
from ui.view.main import Ui_MainWindow


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.open_eml.triggered.connect(self.read_eml)

    def read_eml(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "./", "Eml (*.eml)")
        # 打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
        # 如果用户主动关闭文件对话框，则返回值为空
        if fname[0]:  # 判断路径非空
            f = QFile(fname[0])  # 创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
            # open()会自动返回一个文件对象
            reader = EmlReader(fname[0])
            info = reader.read()
            self.textEdit.setText(info.__str__())
