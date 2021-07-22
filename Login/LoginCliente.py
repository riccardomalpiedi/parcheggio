import sqlite3

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from Login.RegistrazioneNuovoCliente import RegistrazioneNuovoCliente
# from Utente.VistaUtente import VistaUtente
from Utente.VistaProfiloUtente import VistaProfiloUtente


class LoginCliente(QDialog):
    def __init__(self):
        super(LoginCliente, self).__init__()
        loadUi("Login/LoginCliente.ui", self)

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

        if user == "" and password == "" or len(user) == 0 or len(password) == 0:
            QMessageBox.critical(self, 'Errore', "Inserisci tutte le informazioni richieste",
                                       QMessageBox.Ok, QMessageBox.Ok)
        else:
                conn = sqlite3.connect('clienti.db')
                cur = conn.cursor()
                query = 'SELECT password FROM clienti WHERE username =\'' + user + "\'"
                cur.execute(query)
                var = cur.fetchone()[0]
                if var == password:
                    print("Loggato con successo")
                    self.go_vista_profilo_utente()
                    self.close()
                else:
                    QMessageBox.critical(self, 'Errore', "Credenziali inserite errare",
                                         QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_profilo_utente(self):
        self.vista_profilo_utente = VistaProfiloUtente()
        self.vista_profilo_utente.show()

    def go_registrati_function(self):
        self.registrati_function = RegistrazioneNuovoCliente()
        self.registrati_function.show()
        self.close()

    def back_function(self):
        self.close()
