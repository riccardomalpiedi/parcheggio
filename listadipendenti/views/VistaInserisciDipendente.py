from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        loadUi("listadipendenti/views/NuovoDipendente.ui", self)

        self.controller = controller
        self.callback = callback

        self.ok_button.clicked.connect(self.add_dipendente)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Dipendente')

    def add_dipendente(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.codice_fiscale_field.text()
        data_nascita = self.data_nascita_field.text()
        luogo_nascita = self.luogo_nascita_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        licenza = self.licenza_field.text()

        if nome == "" or cognome == "" or cf == "" or data_nascita == "" or luogo_nascita == "" or email == "" or telefono == "" or licenza == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_dipendente(
                Dipendente((nome + cognome).lower(), nome, cognome, cf, data_nascita, luogo_nascita, email, telefono,
                           licenza))
            self.callback()
            self.close()
