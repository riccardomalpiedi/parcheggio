import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        loadUi("Login/RegistrazioneUtente.ui", self)

        self.controller = controller
        self.callback = callback

        self.comboveicoli_model = QStandardItemModel(self.veicolo_comboBox)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                self.lista_veicoli_salvata = pickle.load(f)
            for veicolo in self.lista_veicoli_salvata:
                item = QStandardItem()
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboveicoli_model.appendRow(item)
            self.veicolo_comboBox.setModel(self.comboveicoli_model)

        self.ok_button.clicked.connect(self.add_cliente)
        self.back_button.clicked.connect(self.go_back)

        self.setFixedWidth(736)
        self.setFixedHeight(618)
        self.setWindowTitle("Registrazione Nuovo Cliente")

    def add_cliente(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.codice_fiscale_field.text()
        indirizzo = self.indirizzo_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        veicolo = self.veicolo_comboBox.currentText()
        username = self.username_field.text()
        password = self.password_field.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or veicolo == ""\
                or username == "" or password == "":

            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_cliente(
                Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, veicolo, username,
                        password))

            self.callback()
            self.close()

    def go_back(self):
        self.close()
