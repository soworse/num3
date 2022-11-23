from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
import random
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        c1 = random.randint(1, 255)
        c2 = random.randint(1, 255)
        c3 = random.randint(1, 255)
        qp.setBrush(QColor(c1, c2, c3))
        n1 = random.randint(1, 500)
        n2 = random.randint(1, 500)
        n3 = random.randint(1, 500)
        n4 = random.randint(1, 500)
        qp.drawEllipse(n1, n2, n3, n4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
print(1)