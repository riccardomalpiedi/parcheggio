from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi

from home.views.VistaCliente import VistaCliente
from home.views.VistaHelpButton import VistaHelpButton
from home.views.VistaLogin import LoginScreen


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("easyparking.ui", self)
        self.login_button.clicked.connect(self.go_login_screen)
        self.cliente_button.clicked.connect(self.go_vista_cliente)
        # self.aboutus_button.clicked.connect(self.go_vista_aboutus_button)
        self.help_button.clicked.connect(self.go_vista_help_button)

    # def gotologin(self):
        # login = LoginScreen()
        # widget.addWidget(login)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_vista_cliente(self):
        self.vista_cliente = VistaCliente()
        self.vista_cliente.show()
        # pass

    # def go_vista_aboutus_button(self):
        # self.vista_aboutus_button = VistaAboutusButton()
        # self.vista_aboutus_button.show()
        # pass

    def go_vista_help_button(self):
        self.vista_help_button = VistaHelpButton()
        self.vista_help_button.show()
        # pass

    def go_login_screen(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()