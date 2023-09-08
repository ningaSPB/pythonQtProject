from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connets()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
    def initUI(self):
        pass
    def connets(self):
        pass


