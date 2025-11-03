from PyQt5.QtWidgets import QDialog
import pyperclip
from caesar import Caesar
from forms.message_form import MessageForm
from ui.ui_decryption import UiDecryption


class DecryptionForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UiDecryption()
        self.ui.setupUi(self)
        self.ui.decrypt.clicked.connect(self.decrypt)

    def decrypt(self):
        caesar = Caesar()
        encrypted_text = self.ui.text.text()
        shift = int(self.ui.shift_value.currentText().split(' ')[1])
        decrypted_text = caesar.decrypt(encrypted_text, shift)

        pyperclip.copy(decrypted_text)

        message_window = MessageForm()
        last_text = message_window.ui.result.text()
        message_window.ui.result.setText(f"{last_text} {decrypted_text}")
        message_window.exec_()
