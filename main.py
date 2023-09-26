from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from secondwin import SecondWin
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connets()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(400, 400)
    def initUI(self):
        text = QLabel(txt_hello)
        text1 = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        line = QVBoxLayout()
        line.addWidget(text,alignment=Qt.AlignCenter)
        line.addWidget(text1,alignment=Qt.AlignCenter)
        line.addWidget(self.button)
        self.setLayout(line)
    def connets(self):
        self.button.clicked.connect(self.next)
    def next(self):
        self.secondwin = SecondWin()
        self.hide()


app = QApplication([])
win = MainWin()
app.exec_()