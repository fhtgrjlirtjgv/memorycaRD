from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout ,QRadioButton, QMessageBox

app = QApplication([])
win = QWidget()
win.resize(500,300)
win.setWindowTitle("Конкурс crazy people")
question = QLabel("В якому році народився Шевченко?")

btn_answer = QRadioButton('2005')
btn_answer2 = QRadioButton('1853')
btn_answer3 = QRadioButton('1999')
btn_answer4 = QRadioButton('1814')

v_line = QVBoxLayout()
v_line.addWidget(question, alignment = Qt.AlignCenter)

def winner():
victory_win = QMessageBox()
victory_win.setText('Правильно!')
victory_win.exec_()

row1 = QHBoxLayout()
row2 = QHBoxLayout()

btn_answer4.clicked.connect(winner)

row1.addWidget(btn_answer, alignment = Qt.AlignCenter)
row1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
row2.addWidget(btn_answer3, alignment = Qt.AlignCenter)
row2.addWidget(btn_answer4, alignment = Qt.AlignCenter)

v_line.addLayout(row1)
v_line.addLayout(row2)


win.setLayout(v_line)
win.show()
app.exec_()

