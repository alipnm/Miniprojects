from PyQt5.QtWidgets import QDialog
import pyperclip
from caesar import Caesar
from forms.message_form import MessageForm
from ui.ui_encryption import UiEcryption


class EncryptionForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UiEcryption()
        self.ui.setupUi(self)
        self.caesar = Caesar()

        self.ui.encryption.clicked.connect(self.encrypt)

    def encrypt(self):
        hashed = self.caesar.encrypt(
            self.ui.text.text(), int(
                self.ui.shift_value.currentText().split(' ')[1]
            )
        )
        pyperclip.copy(hashed)

        message_window = MessageForm()
        last_text = message_window.ui.result.text()
        message_window.ui.result.setText(f"{last_text} {hashed}")
        message_window.exec_()
