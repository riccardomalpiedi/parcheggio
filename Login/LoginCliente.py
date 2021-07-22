
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from Utente.VistaProfiloUtente import VistaProfiloUtente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente


class LoginCliente(QDialog):
    def __init__(self):
        super(LoginCliente, self).__init__()
        loadUi("Login/LoginCliente.ui", self)
        self.controller = ControlloreListaClienti()

        self.setFixedHeight(484)
        self.setFixedWidth(635)
        self.setWindowTitle("Login")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
        self.registrati_button.clicked.connect(self.go_registrati_function)
        self.back_button.clicked.connect(self.back_function)

    def login_funcion(self):
        user = self.username_field.text()
        password = self.password_field.text()

        flag = False
        if user == "" and password == "" or len(user) == 0 or len(password) == 0:
            QMessageBox.critical(self, "Errore", "Inserisci tutte le informazioni richieste",
                                   QMessageBox.Ok, QMessageBox.Ok)
        else:
            for cliente in self.controller.get_lista_dei_clienti():
                if user == cliente.username:
                    if password == cliente.password:
                        print("Loggato con successo")
                        self.go_vista_profilo_utente()
                        self.close()
                        flag = True
        if flag == False:
            QMessageBox.critical(self, 'Errore', "credenziali errate",
                                         QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_profilo_utente(self):
        self.vista_profilo_utente = VistaProfiloUtente()
        self.vista_profilo_utente.show()

    def go_registrati_function(self):
        self.registrati_function = VistaInserisciCliente(self.controller, self.update_ui)
        self.registrati_function.show()
        self.close()

    def back_function(self):
        self.close()

    def update_ui(self):
        pass