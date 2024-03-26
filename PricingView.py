from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMainWindow

from BlackScholes import BlackScholes


class PricingWindow(QMainWindow):
    show_main_win_signal = pyqtSignal()

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.pw = PricingWidget(main, self)
        self.setCentralWidget(self.pw)

        self.adjustSize()
        self.resize(800, 500)


class PricingWidget(QWidget):  # 显示各种结果曲线、拍摄视频的页面
    def __init__(self, main, pricing):
        super().__init__()
        self.main = main
        self.main.cw.paras.connect(self.handle_signal)
        self.pricing = pricing

        self.ui = uic.loadUi('PricingView.ui', self)

        self.ui.back_button.clicked.connect(self.go_back)
        self.ui.pricing_button.clicked.connect(self.calculate)

    def enable_all(self):
        self.ui.input_v.setDisabled(False)
        self.ui.input_q.setDisabled(False)
        self.ui.input_n.setDisabled(False)
        self.ui.input_m.setDisabled(False)
        self.ui.input_s1.setDisabled(False)
        self.ui.input_sigma1.setDisabled(False)
        self.ui.input_rho.setDisabled(False)
        self.ui.input_L.setDisabled(False)
        self.ui.input_U.setDisabled(False)
        self.ui.input_R.setDisabled(False)
        self.ui.choose_control.setDisabled(False)
        self.ui.input_sigma0.setDisabled(False)

    def initial(self):
        # ["Black-Sholes Formulas for European option", "Implied Volatility",
        #  "Closed-form Formulas for Geometric Asian Options ",
        #  "Closed-form Formulas for Geometric Basket Options ",
        #  "Monte Carlo with Control Variate for Arithmetic Asian Options",
        #  "Monte Carlo with Control Variate for Arithmetic Basket Options",
        #  "Quasi-Monte Carlo for KIKO-put Option",
        #  "Binomial Tree for American Option"]

        self.enable_all()

        if self.option_index == 0:  # Black-Sholes Formulas for European option
            self.ui.input_v.setDisabled(True)
            self.ui.input_n.setDisabled(True)
            self.ui.input_m.setDisabled(True)
            self.ui.input_s1.setDisabled(True)
            self.ui.input_sigma1.setDisabled(True)
            self.ui.input_rho.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.choose_control.setDisabled(True)
        elif self.option_index == 1:  # Implied Volatility
            self.ui.input_sigma0.setDisabled(True)
            self.ui.input_n.setDisabled(True)
            self.ui.input_m.setDisabled(True)
            self.ui.input_s1.setDisabled(True)
            self.ui.input_sigma1.setDisabled(True)
            self.ui.input_rho.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.choose_control.setDisabled(True)
        elif self.option_index == 2:  # Closed-form Formulas for Geometric Asian Options
            self.ui.input_q.setDisabled(True)
            self.ui.input_m.setDisabled(True)
            self.ui.input_s1.setDisabled(True)
            self.ui.input_sigma1.setDisabled(True)
            self.ui.input_rho.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.choose_control.setDisabled(True)
            self.ui.input_v.setDisabled(True)

        elif self.option_index == 3:  # Closed-form Formulas for Geometric Basket Options
            self.ui.input_q.setDisabled(True)
            self.ui.input_m.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.input_v.setDisabled(True)

            self.ui.choose_control.setDisabled(True)
        elif self.option_index == 4:  # Monte Carlo with Control Variate for Arithmetic Asian Options
            self.ui.input_q.setDisabled(True)
            self.ui.input_s1.setDisabled(True)
            self.ui.input_sigma1.setDisabled(True)
            self.ui.input_rho.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.input_v.setDisabled(True)

        elif self.option_index == 5:  # Monte Carlo with Control Variate for Arithmetic Basket Options
            self.ui.input_q.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.input_v.setDisabled(True)
        else:  # Binomial Tree for American Option
            self.ui.input_v.setDisabled(True)
            self.ui.input_q.setDisabled(True)
            self.ui.input_m.setDisabled(True)
            self.ui.input_s1.setDisabled(True)
            self.ui.input_sigma1.setDisabled(True)
            self.ui.input_rho.setDisabled(True)
            self.ui.input_L.setDisabled(True)
            self.ui.input_U.setDisabled(True)
            self.ui.input_R.setDisabled(True)
            self.ui.choose_control.setDisabled(True)

    def go_back(self):
        self.pricing.show_main_win_signal.emit()

    def handle_signal(self, paras):
        self.option_index = paras[0]
        self.type = paras[1]
        print(paras)
        self.initial()

    def calculate(self):
        self.get_values()

        if self.option_index == 0:  # Black-Sholes Formulas for European option
            bs = BlackScholes(self.s0, self.sigma0, self.r, self.q, self.T, self.K, self.type)
            result = bs.get_result()
            self.ui.result_label.setText(str(result))
        elif self.option_index == 1:  # Implied Volatility
            n = 1
        elif self.option_index == 2:  # Closed-form Formulas for Geometric Asian Options
            n = 1
        elif self.option_index == 3:  # Closed-form Formulas for Geometric Basket Options
            n = 1
        elif self.option_index == 4:  # Monte Carlo with Control Variate for Arithmetic Asian Options
            n = 1
        elif self.option_index == 5:  # Monte Carlo with Control Variate for Arithmetic Basket Options
            n = 1
        else:  # Binomial Tree for American Option
            n = 1

    def get_values(self):
        self.s0 = self.ui.input_s0.toPlainText()
        self.s1 = self.ui.input_s1.toPlainText()
        self.sigma0 = self.ui.input_sigma0.toPlainText()
        self.sigma1 = self.ui.input_sigma1.toPlainText()
        self.rho = self.ui.input_rho.toPlainText()

        self.K = self.ui.input_K.toPlainText()
        self.L = self.ui.input_L.toPlainText()
        self.R = self.ui.input_R.toPlainText()
        self.T = self.ui.input_T.toPlainText()
        self.U = self.ui.input_U.toPlainText()
        self.m = self.ui.input_m.toPlainText()
        self.n = self.ui.input_n.toPlainText()
        self.q = self.ui.input_q.toPlainText()
        self.r = self.ui.input_r.toPlainText()
