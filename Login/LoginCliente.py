import sqlite3

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from Utente.VistaUtente import VistaUtente


class LoginCliente(QDialog):
    def __init__(self):
        super(LoginCliente, self).__init__()
        loadUi("Login/LoginCliente.ui", self)

        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowTitle("Login")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_funcion)
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
                self.go_vista_utente()
                self.close()
            else:
                QMessageBox.critical(self, 'Errore', "Credenziali inserite errate",
                                     QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_utente(self):
        self.vista_utente = VistaUtente()
        self.vista_utente.show()

    def back_function(self):
        self.close()
