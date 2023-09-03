from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
def show_winer():
    winner = randint(1, 100)
    label1.setText(str(winner))

app = QApplication([])
mw = QWidget()
mw.show()
mw.setWindowTitle('кот')
label = QLabel('нажми чтобы узнать победителя')
vline = QVBoxLayout()
vline.addWidget(label,alignment= Qt.AlignCenter)
button = QPushButton('нажми')
button.clicked.connect(show_winer)
label1 = QLabel('?')
vline.addWidget(label1,alignment= Qt.AlignCenter)
vline.addWidget(button,alignment= Qt.AlignCenter)

mw.setLayout(vline)
app.exec_()

