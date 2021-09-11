from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from home.views.VistaHomeCliente import VistaHomeCliente
from home.views.VistaHelpButton import VistaHelpButton
from home.views.VistaLogin import LoginScreen


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("easyparking.ui", self)

        self.setWindowIcon(QIcon("icone/parking2.png"))

        self.login_button.clicked.connect(self.go_login_screen)
        self.cliente_button.clicked.connect(self.go_vista_cliente)
        self.help_button.clicked.connect(self.go_vista_help_button)

    def go_vista_cliente(self):
        self.vista_cliente = VistaHomeCliente()
        self.vista_cliente.show()

    def go_vista_help_button(self):
        self.vista_help_button = VistaHelpButton()
        self.vista_help_button.show()

    def go_login_screen(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()
