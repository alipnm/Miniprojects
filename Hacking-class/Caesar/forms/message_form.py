from PyQt5.QtWidgets import QDialog
from ui.ui_message import UiMessage


class MessageForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UiMessage()
        self.ui.setupUi(self)
