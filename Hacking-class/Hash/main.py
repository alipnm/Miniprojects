import sys
from PyQt5.QtWidgets import QApplication
from forms.main_form import MainForm

app = QApplication(sys.argv)

main_window = MainForm()
main_window.exec_()
