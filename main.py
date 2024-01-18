import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPainter


class AlphaManagement(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('Ui.ui', self)  # Загружаем дизайн

        self.color = QColor(250, 250, 0)
        self.painter = QPainter()
        self.do_draw = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            self.painter.begin(self)
            self.painter.setBrush(self.color)
            self.painter.eraseRect(self.rect())
            r = randint(20, 100)
            center = QtCore.QPointF(randint(r, self.width() - r),
                                    randint(self.pushButton.height() + r, self.height() - r))
            self.painter.drawEllipse(center, r, r)
            self.painter.end()
            self.do_draw = False


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec_())
