from PyQt6 import QtWidgets, uic
import sys

class Login(QtWidgets.QMainWindow):
    __init__(self):
    super().__init__()
    uic.loadUi("./views/login.ui", self)

    class (QtWidgets.QMainWindow):
    __init__(self):
    super().__init__()
    uic.loadUi("./views/main.ui" self)

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.sell_window = sell()
        #muestra la pantalla
        self.login_window.show()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
    sys.exit(app.exec())
