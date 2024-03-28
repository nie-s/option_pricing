from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QComboBox, QLabel, QTextEdit


class MainWidget(QWidget):
    paras = pyqtSignal(list)
    # option_index = pyqtSignal(str)

    def __init__(self, w):
        super().__init__()

        self.w = w

        # Use a grid layout
        self.layout = QtWidgets.QGridLayout()
        self.layout.setAlignment(Qt.AlignHCenter)
        self.layout.setSpacing(20)

        self.setLayout(self.layout)

        self.choose_label = QLabel(self)
        self.choose_label.setText(str('Choose one method:'))
        self.choose_label.setFixedSize(150, 35)

        self.choose_box = QComboBox(self)
        self.choose_box.setFixedSize(300, 35)
        self.choose_box.addItems(["Black-Sholes Formulas for European option", "Implied Volatility",
                                  "Closed-form Formulas for Geometric Asian Options ",
                                  "Closed-form Formulas for Geometric Basket Options ",
                                  "Monte Carlo with Control Variate for Arithmetic Asian Options",
                                  "Monte Carlo with Control Variate for Arithmetic Basket Options",
                                  "Quasi-Monte Carlo for KIKO-put Option",
                                  "Binomial Tree for American Option"])

        self.type_label = QLabel(self)
        self.type_label.setText(str('Option type:'))
        self.type_label.setFixedSize(150, 35)

        self.type_box = QComboBox(self)
        self.type_box.setFixedSize(300, 35)
        self.type_box.addItems(["put", "call", ])

        self.confirm_button = QtWidgets.QPushButton(self)
        self.confirm_button.setText('Confirm')
        self.confirm_button.setGeometry(350, 350, 100, 40)
        self.confirm_button.clicked.connect(self.confirm)

        self.layout.addWidget(self.choose_label, 0, 1)
        self.layout.addWidget(self.choose_box, 0, 2)
        self.choose_box.currentIndexChanged.connect(self.on_choose_box_changed)

        self.layout.addWidget(self.type_label, 1, 1)
        self.layout.addWidget(self.type_box, 1, 2)


    def on_choose_box_changed(self, index):
        if self.choose_box.currentText() == "Quasi-Monte Carlo for KIKO-put Option":
            if "call" in [self.type_box.itemText(i) for i in range(self.type_box.count())]:
                self.type_box.removeItem(self.type_box.findText("call"))
        else:
            if "call" not in [self.type_box.itemText(i) for i in range(self.type_box.count())]:
                self.type_box.addItem("call")


    def confirm(self):
        option_type = self.type_box.currentText()
        option_index = self.choose_box.currentIndex()

        self.w.show_pricing_win_signal.emit()

        self.paras.emit([option_index,  option_type])

        # step 1: choose one method
        # step 2: disable parameters
        # step 3: pass parameters (method, put/call)
