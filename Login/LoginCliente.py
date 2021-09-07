
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

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Login")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
        self.registrati_button.clicked.connect(self.go_vista_inserisci_cliente)
        self.back_button.clicked.connect(self.back_function)

    def login_funcion(self):
        user = self.username_field.text()
        password = self.password_field.text()

        if user == "" and password == "" or len(user) == 0 or len(password) == 0:
            QMessageBox.critical(self, "Errore", "Inserisci tutte le informazioni richieste",
                                   QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            for cliente in self.controller.get_lista_dei_clienti():
                if user == cliente.username:
                    if password == cliente.password:
                        print("Loggato con successo")
                        self.go_vista_profilo_utente(cliente)
                        self.close()
                        return
        QMessageBox.critical(self, 'Errore', "credenziali errate", QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_profilo_utente(self, cliente):
        self.vista_profilo_utente = VistaProfiloUtente(cliente)
        self.vista_profilo_utente.show()

    def go_vista_inserisci_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()
        self.close()

    def back_function(self):
        self.close()

    def update_ui(self):
        pass
