
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from Utente.VistaProfiloUtente import VistaProfiloUtente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class LoginCliente(QDialog):
    def __init__(self):
        super(LoginCliente, self).__init__()
        loadUi("home/LoginCliente2.ui", self)
        self.controller = ControlloreListaClienti()

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
        self.back_button.clicked.connect(self.back_function)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Login")

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
                        self.go_vista_profilo_utente(cliente)
                        self.username_field.setText('')
                        self.password_field.setText('')
                        return
        QMessageBox.critical(self, 'Errore', "Credenziali errate", QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_profilo_utente(self, cliente):
        self.vista_profilo_utente = VistaProfiloUtente(cliente, self.update_list)
        self.vista_profilo_utente.show()

    def update_list(self):
        self.controller.save_data()

    def back_function(self):
        self.close()
