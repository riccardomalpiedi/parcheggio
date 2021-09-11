from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from home.views.VistaAmministratore import VistaAmministratore
from home.views.VistaCassiere import VistaCassiere


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_function)
        self.back_button.clicked.connect(self.back_function)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Login")

    def login_function(self):
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
                    QMessageBox.critical(self, 'Errore', 'Le informazioni inserite non sono corrette. Ricontrolla!!!',
                                         QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_amministratore(self):
        self.vista_amministratore = VistaAmministratore()
        self.vista_amministratore.show()

    def go_vista_cassiere(self):
        self.vista_dipendente = VistaCassiere()
        self.vista_dipendente.show()

    def back_function(self):
        self.close()
