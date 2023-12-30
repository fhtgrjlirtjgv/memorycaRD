from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([]) #сторюємо віконний додаток

from window import*

win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)

def answer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступне питання")
    else:
        group_box.show()
        result_box.hide()
        answer_btn.setText("Наступне питання")

answer_btn.clicked.connect(answer_click)

# вкінці
win.show() #показує вікно
app.exec_() # запускаємо додаток