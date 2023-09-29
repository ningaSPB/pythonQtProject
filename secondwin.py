from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
from finalwin import FinalWin as Final

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connets()
        self.show()

    def initUI(self):
        text_name = QLabel(txt_name)
        line_l = QVBoxLayout()
        line_l.addWidget(text_name, alignment=Qt.AlignLeft)
        input_name = QLineEdit('Имя')
        line_l.addWidget(input_name, alignment=Qt.AlignLeft)
        text_age = QLabel(txt_age)
        line_l.addWidget(text_age, alignment=Qt.AlignLeft)
        input_age = QLineEdit('0')
        line_l.addWidget(input_age, alignment=Qt.AlignLeft)
        text_exercise = QLabel(txt_test1)
        line_l.addWidget(text_exercise, alignment=Qt.AlignLeft)
        self.button = QPushButton(txt_starttest1)
        line_l.addWidget(self.button, alignment=Qt.AlignLeft)
        result = QLineEdit('0')
        line_l.addWidget(result, alignment=Qt.AlignLeft)
        task = QLabel(txt_test2)
        line_l.addWidget(task, alignment=Qt.AlignLeft)
        self.button_exercise = QPushButton(txt_starttest2)
        line_l.addWidget(self.button_exercise, alignment=Qt.AlignLeft)
        text_exercise1 = QLabel(txt_test3)
        line_l.addWidget(text_exercise1, alignment=Qt.AlignLeft)
        self.button_finish = QPushButton(txt_starttest3)
        line_l.addWidget(self.button_finish, alignment=Qt.AlignLeft)

        result1 = QLineEdit('0')
        line_l.addWidget(result1, alignment=Qt.AlignLeft)
        result2 = QLineEdit('0')
        line_l.addWidget(result2, alignment=Qt.AlignLeft)



        self.finish = QPushButton(txt_sendresults)
        line_l.addWidget(self.finish, alignment=Qt.AlignCenter)

        line_r = QVBoxLayout()

        line_h = QHBoxLayout()
        line_h.addLayout(line_l)
        line_h.addLayout(line_r)

        self.text_timer = QLabel(txt_timer)
        line_r.addWidget(self.text_timer)

        self.setLayout(line_h)



    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def timer1_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('ss')=='00':
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)

    def timer2_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('ss'))
        if time.toString('ss') == '00':
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def connets(self):
        self.finish.clicked.connect(self.next)
        self.button.clicked.connect(self.timer_test)
        self.button_exercise.clicked.connect(self.timer_sits)
        self.button_finish.clicked.connect(self.timer_final)

    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(400, 400)

    def next(self):
        self.finalwin = Final()
        self.hide()
