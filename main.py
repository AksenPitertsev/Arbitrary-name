import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        button = QPushButton("Создать", self)
        button.move(100, 100)
        button.clicked.connect(self.createYellowCircle)

        self.setFixedSize(300, 300)
        self.setWindowTitle("Yellow circle")
        self.resize(300, 300)

    def createYellowCircle(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 255, 0))
        x = random.randint(0, 250)
        y = random.randint(0, 250)
   w = random.randint(20, 50)
        painter.drawEllipse(x, y, w, w)


app = QApplication(sys.argv)
myWidget = MyWidget()
myWidget.show()
sys.exit(app.exec_())
