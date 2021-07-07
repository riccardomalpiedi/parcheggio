from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from home.views.VistaAmministratore import VistaAmministratore
from home.views.VistaCassiere import VistaCassiere


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowTitle("Login")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
        self.back_button.clicked.connect(self.back_function)

    def login_funcion(self):
        user = self.email_field.text()
        password = self.password_field.text()

        if user == "aaaa" and password == "bbbb":
            self.go_vista_amministratore()
            self.close()
        else:
            if user == "cccc" and password == "dddd":
                self.go_vista_cassiere()
                self.close()
            else:
                if user == "" and password == "" or len(user) == 0 or len(password) == 0:
                    QMessageBox.critical(self, 'Errore', "Inserisci tutte le informazioni richieste",
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, 'Errore', 'Controlla meglio quello che hai scritto perche non va',
                                         QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_amministratore(self):
        self.vista_amministratore = VistaAmministratore()
        # self.setWindowIcon(QIcon("administrator2.png"))
        self.vista_amministratore.show()
        # pass

    def go_vista_cassiere(self):
        self.vista_dipendente = VistaCassiere()
        self.vista_dipendente.show()
        # pass

    def back_function(self):
        self.close()