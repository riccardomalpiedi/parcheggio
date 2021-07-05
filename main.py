import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi

from home.views.VistaAboutusButton import VistaAboutusButton
from home.views.VistaAmministratore import VistaAmministratore
from home.views.VistaCassiere import VistaCassiere
from home.views.VistaCliente import VistaCliente
from home.views.VistaHelpButton import VistaHelpButton


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("easyparking.ui", self)
        self.login_button.clicked.connect(self.gotologin)
        self.cliente_button.clicked.connect(self.go_vista_cliente)
        self.aboutus_button.clicked.connect(self.go_vista_aboutus_button)
        self.help_button.clicked.connect(self.go_vista_help_button)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_vista_cliente(self):
        self.vista_cliente = VistaCliente()
        self.vista_cliente.show()
        # pass

    def go_vista_aboutus_button(self):
        self.vista_aboutus_button = VistaAboutusButton()
        self.vista_aboutus_button.show()
        # pass

    def go_vista_help_button(self):
        self.vista_help_button = VistaHelpButton()
        self.vista_help_button.show()
        # pass

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
        self.back_button.clicked.connect(self.return_main_screen)

    def login_funcion(self):
        user = self.email_field.text()
        password = self.password_field.text()

        if user == "aaaa" and password == "bbbb":
            self.go_vista_amministratore()
            # self.close()
        else:
            if user == "cccc" and password == "dddd":
                self.go_vista_cassiere()
                # self.close()
            else:
                if user == "" and password == "" or len(user) == 0 or len(password) == 0:
                    QMessageBox.critical(self, 'Errore', 'Controlla meglio quello che hai scritto perche non va',
                                        QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, 'Errore', 'Controlla meglio quello che hai scritto perche non va',
                                         QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_amministratore(self):
        self.vista_amministratore = VistaAmministratore()
        self.vista_amministratore.show()
        # pass

    def go_vista_cassiere(self):
        self.vista_dipendente = VistaCassiere()
        self.vista_dipendente.show()
        # pass

    def return_main_screen(self):
        login = LoginScreen()
        widget.removeWidget(login)
        widget.setCurrentIndex(widget.currentIndex() - 1)

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
