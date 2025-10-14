from PyQt5.QtWidgets import QDialog
from ui.ui_main import MainUi


class MainForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = MainUi()
        self.ui.setupUi(self)
        self.ui.encrypt.clicked.connect(self.encrypt)
        self.ui.decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        pass

    def decrypt(self):
        pass
