from PyQt5.QtWidgets import QDialog
from ui.ui_main import Ui_Encrypt


class MainForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Encrypt()
        self.ui.setupUi(self)
