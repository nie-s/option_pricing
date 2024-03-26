import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

from MainWidget import MainWidget
from PricingView import PricingWindow


class MainWindow(QMainWindow):
    show_pricing_win_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.adjustSize()
        self.resize(800, 500)

        self.cw = MainWidget(self)
        self.setCentralWidget(self.cw)

        self.show()


def show_pricing():
    pricing.show()
    main.hide()


def show_main():
    main.show()
    pricing.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    pricing = PricingWindow(main)
    main.show_pricing_win_signal.connect(show_pricing)
    pricing.show_main_win_signal.connect(show_main)
    app.exec_()
