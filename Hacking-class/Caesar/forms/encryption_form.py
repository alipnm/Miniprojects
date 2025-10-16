from ui.ui_encryption import Ui_Ecryption
from PyQt5.QtWidgets import QDialog
from caesar import Caesar


class EncryptionForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Ecryption()
        self.ui.setupUi(self)
        self.caesar = Caesar()

        self.ui.encryption.clicked.connect(self.encrypt)

    def encrypt(self):
        pass
