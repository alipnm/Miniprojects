import sys
from PyQt5.QtWidgets import QApplication
from forms.encryption_form import EncryptionForm
from forms.main_form import MainForm

app = QApplication(sys.argv)
main_window = MainForm()

run = main_window.exec_()

if run == MainForm.Accepted:
    encryption_window = EncryptionForm()
    encryption_window.exec_()
elif run == MainForm.Rejected:
    pass
