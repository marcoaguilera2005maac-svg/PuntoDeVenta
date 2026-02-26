#pip install pyqt6 pyqt6-tools
#.\venv\Scripts\Activate.ps1 (activar el entorno virtual)
from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)
class Sell(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui", self)

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.sell_window = Sell()
        #muestra la pantalla
        self.login_window.show()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())