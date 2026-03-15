#pip install pyqt6 pyqt6-tools
#.\venv\Scripts\Activate.ps1 (activar el entorno virtual)¿
from urllib import request
from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette


class Login(QtWidgets.QMainWindow):
    login_successfull = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)
        self.apply_theme()

    def apply_theme(self):
        is_dark = self.palette().color(QPalette.ColorRole.Window).lightness() < 128
        print(f"Is dark theme: {is_dark}")

class Sell(QtWidgets.QMainWindow):
    request_payment = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui", self)
        self.btn_cobrar.clicked.connect(lambda:self.request_payment.emit())

class Payment(QtWidgets.QDialog):
    def __init__ (self):
        super().__init__()
        uic.loadUi("./views/payment.ui", self)


class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.sell_window = Sell()
        self.payment_dialog = Payment()
        self.login_window.login_successfull.connect(self.show_main_window)
        self.sell_window.request_payment.connect(self.show_payment)
        self.login_window.show()
        #muestra la pantalla
        self.login_window.show()
    
    def show_main_window(self):
        self.sell_window.show() #mostrar ventana de venta
        self.login_window.close() #cerramos la ventana

    def show_payment(self):
        self.payment_dialog.show()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())