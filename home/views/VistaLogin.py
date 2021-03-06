from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from home.controller.ControlloreLogin import ControlloreLogin
from home.views.VistaAmministratore import VistaAmministratore
from home.views.VistaCassiere import VistaCassiere


# schermata di login per il personale (amministratore e cassiere)
class VistaLogin(QDialog):
    def __init__(self):
        super(VistaLogin, self).__init__()
        loadUi("home/views/VistaLogin.ui", self)

        self.controller = ControlloreLogin()

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_function)
        self.back_button.clicked.connect(self.back_function)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Login")

    # metodo per il login: se le credenziali sono giuste, si aprirà la schermata dell'amministratore/cassiere
    def login_function(self):
        user = self.email_field.text()
        password = self.password_field.text()

        id = self.controller.login_function(user, password)

        if id == "Amministratore":
            self.go_vista_amministratore()
            self.close()
        else:
            if id == "Cassiere":
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
