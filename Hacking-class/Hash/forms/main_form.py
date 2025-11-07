from PyQt5.QtWidgets import QDialog, QMessageBox
import pyperclip
from hash_machine import HashMachine
from ui.ui_main import Ui_Encrypt


class MainForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Encrypt()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.encrypt)

    def encrypt(self):
        text = self.ui.lineEdit.text()
        sha_func = self.ui.comboBox.currentText()

        machine = HashMachine()
        encrypted_text = machine.encrypt(sha_func.lower(), text)

        pyperclip.copy(encrypted_text)
        self.ui.lineEdit.setText("")
        QMessageBox.about(
            self, "Encrypted", f"The encrypted password is: {encrypted_text}\nCopied to clipboard."
        )
