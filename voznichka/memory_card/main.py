from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout ,QRadioButton, QMessageBox

app = QApplication([])

from main_window import main_line

win = QWidget()
win.resize(500,300)
win.setWindowTitle("MemorycaRD")
win.setLayout(main_line)

win.show()
app.exec_()