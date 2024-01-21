from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice, shuffle
from time import sleep
app = QApplication([]) #сторюємо віконний додаток

from window import*
from menu import*

class Question():
    current = None

    def __init__(self, text, right_ans, ans2, ans3, ans4):
        self.text = text
        self.right_ans = right_ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4


question = [
    Question("вісім", "eight", "eit", "eidhgt", "nine"),
    Question("чотири", "four", "fove", "fare", "foure"),
    Question("три", "three", "tri", "try", "troy"),
    Question("один", "one", "oni", "onene", "odun"),
    Question("два", "two", "the", "thy", "thoo"),
    ]

radio_list = [btn1, btn2, btn3, btn4]

win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)

def next_question():
    
    Question.current = choice(question)
    question_lb.setText(Question.current.text)
    shuffle(radio_list)
    radio_list[0].setText(Question.current.right_ans)
    radio_list[1].setText(Question.current.ans2)
    radio_list[2].setText(Question.current.ans3)
    radio_list[3].setText(Question.current.ans4)


def check_answer():
    if radio_list[0].isChecked():
        result_text.setText("Правильно")
    else:
        result_text.setText("Неправильно")

    radio_group.setExclusive(False)
    for btn in radio_list:
        btn.setChecked(False)
    radio_group.setExclusive(True)

def answer_click():
    if answer_btn.text() == "Відповісти":
        if radio_group.checkedButton():
            check_answer()
            group_box.hide()
            result_box.show()
            answer_btn.setText("Наступне питання")
    else:
        next_question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")
        
def show_menu():
    win.hide()
    menu_win.show()

def hide_menu():
    win.show()
    menu_win.hide()

def relax():
    pause_time = int(time_spin.value()) * 60
    win.hide()
    sleep(pause_time)
    win.show()


answer_btn.clicked.connect(answer_click)
menu_btn.clicked.connect(show_menu)
back_btn.clicked.connect(hide_menu)
rest_btn.clicked.connect(relax)

next_question()
# вкінці
next_question()
win.show() #показує вікно
app.exec_() # запускаємо додаток













