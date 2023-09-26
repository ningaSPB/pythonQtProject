from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *

class Final(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(400, 400)

    def initUI(self):
        line_l = QVBoxLayout()
        text = QLabel('Q7')
        line_l.addWidget(text, alignment=Qt.AlignCenter)


        text1 = QLabel('GG')
        line_l.addWidget(text1, alignment=Qt.AlignCenter)

        self.setLayout(line_l)
