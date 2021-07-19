import sqlite3

from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
from listaclienti.views.VistaListaClienti import VistaListaClienti


class RegistrazioneNuovoCliente(QDialog):
    def __init__(self):
        super(RegistrazioneNuovoCliente, self).__init__()
        self.vista_lista_clienti = VistaListaClienti()
        loadUi("Login/RegistrazioneNuovoCliente.ui", self)

        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowTitle("Registrazione")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conferma_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registrati_button.clicked.connect(self.go_registrazione_primaria_function)
        self.back_button.clicked.connect(self.back_function)

    def go_registrazione_primaria_function(self):
        user = self.username_field.text()
        password = self.password_field.text()
        conferma_password = self.conferma_password_field.text()

        if len(user) == 0 or len(password) == 0 or len(conferma_password) == 0:
            QMessageBox.critical(self, 'Errore', "Inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if password != conferma_password:
                QMessageBox.critical(self, 'Errore', "Password non combacianti. Riprova!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                conn = sqlite3.connect("clienti.db")
                cur = conn.cursor()

                user_info = [user, password]
                cur.execute('INSERT INTO clienti (username, password) VALUES(?,?)', user_info)

                conn.commit()
                conn.close()

                self.go_registrazione_completa()

    def go_registrazione_completa(self):
        self.registrazione_function = VistaInserisciCliente(self.vista_lista_clienti.controller,
                                                            self.vista_lista_clienti.update_ui)
        self.registrazione_function.show()

    def back_function(self):
        self.close()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.vista_lista_clienti.controller.save_data()
        event.accept()
