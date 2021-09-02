import os
import pickle
import random
import shutil

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.uic import loadUi

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        loadUi("Login/RegistrazioneUtente.ui", self)

        self.controller = controller
        self.callback = callback

        self.comboveicoli_model = QStandardItemModel(self.veicolo_comboBox)
        item = QStandardItem()
        item.setText("")
        item.setEditable(False)
        self.comboveicoli_model.appendRow(item)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                self.lista_veicoli_salvata = pickle.load(f)
            self.lista_veicoli_disponibili = [c for c in self.lista_veicoli_salvata if not c.get_associato()]
            for veicolo in self.lista_veicoli_disponibili:
                item = QStandardItem()
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboveicoli_model.appendRow(item)
            self.veicolo_comboBox.setModel(self.comboveicoli_model)

        self.comboveicoli2_model = QStandardItemModel(self.veicolo2_comboBox)
        item = QStandardItem()
        item.setText("")
        item.setEditable(False)
        self.comboveicoli2_model.appendRow(item)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            for veicolo in self.lista_veicoli_disponibili:
                item = QStandardItem()
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboveicoli2_model.appendRow(item)
            self.veicolo2_comboBox.setModel(self.comboveicoli2_model)

        self.ok_button.clicked.connect(self.add_cliente)
        self.back_button.clicked.connect(self.go_back)
        self.browse_button.clicked.connect(self.go_browse)

        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.setWindowTitle("Registrazione Nuovo Cliente")

    def add_cliente(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.codice_fiscale_field.text()
        indirizzo = self.indirizzo_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        if self.veicolo_comboBox.currentIndex() == 0:
            veicolo = None
        else:
            veicolo = self.lista_veicoli_disponibili[self.veicolo_comboBox.currentIndex()-1]
        if self.veicolo2_comboBox.currentIndex() == 0:
            veicolo2 = None
        else:
            veicolo2 = self.lista_veicoli_disponibili[self.veicolo2_comboBox.currentIndex()-1]
        username = self.username_field.text()
        password = self.password_field.text()
        image = self.immagine_profilo_field.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" \
                or username == "" or password == "":

            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if veicolo == veicolo2 and veicolo is not None:
                QMessageBox.critical(self, 'Errore', "Inserisci due targhe diverse",
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
            else:
                if image == "":
                    self.controller.aggiungi_cliente(
                        Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, veicolo,
                                veicolo2, username, password, image="Utente/placeholder-user-photo.png"))
                else:
                    self.controller.aggiungi_cliente(
                        Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, veicolo,
                                veicolo2, username, password, image))
                if veicolo is not None:
                    for veicolo_in_lista in self.lista_veicoli_salvata:
                        if veicolo_in_lista.targa == veicolo.targa:
                            veicolo_in_lista.set_associato(True)
                if veicolo2 is not None:
                    for veicolo_in_lista in self.lista_veicoli_salvata:
                        if veicolo_in_lista.targa == veicolo2.targa:
                            veicolo_in_lista.set_associato(True)
                with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.lista_veicoli_salvata, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()

    def go_back(self):
        self.close()

    def go_browse(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:', 'Images (*.png *.xmp *.jpg)')
        var = fname[0]
        print(var)
        rand = random.randint(1, 45697)
        var2 = "Utente/ImmaginiProfilo/" + str(rand) + ".png"
        shutil.copyfile(var, var2)
        print(var2)
        self.immagine_profilo_field.setText(var2)

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
