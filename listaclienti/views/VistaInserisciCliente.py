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
            self.set_combobox_veicoli(self.comboveicoli_model, self.veicolo_comboBox)

        self.comboveicoli2_model = QStandardItemModel(self.veicolo2_comboBox)
        item = QStandardItem()
        item.setText("")
        item.setEditable(False)
        self.comboveicoli2_model.appendRow(item)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            self.set_combobox_veicoli(self.comboveicoli2_model, self.veicolo2_comboBox)

        self.ok_button.clicked.connect(self.add_cliente)
        self.back_button.clicked.connect(self.go_back)
        self.browse_button.clicked.connect(self.go_browse)

        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.setWindowTitle("Registrazione Nuovo Cliente")

    def set_combobox_veicoli(self, comboveicoli_model, veicolo_combobox):
        for veicolo in self.lista_veicoli_disponibili:
            item = QStandardItem()
            item.setText(veicolo.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            comboveicoli_model.appendRow(item)
        veicolo_combobox.setModel(self.comboveicoli_model)

    def add_cliente(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.codice_fiscale_field.text()
        indirizzo = self.indirizzo_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        lista_veicoli = []
        if self.veicolo_comboBox.currentIndex() != 0:
            lista_veicoli.append(self.lista_veicoli_disponibili[self.veicolo_comboBox.currentIndex()-1])
        if self.veicolo2_comboBox.currentIndex() != 0:
            lista_veicoli.append(self.lista_veicoli_disponibili[self.veicolo2_comboBox.currentIndex()-1])
        username = self.username_field.text()
        password = self.password_field.text()
        image = self.immagine_profilo_field.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" \
                or username == "" or password == "":

            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if lista_veicoli is not None and len(lista_veicoli) == 2 and lista_veicoli[0] == lista_veicoli[1]:
                QMessageBox.critical(self, 'Errore', "Inserisci due targhe diverse",
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
            else:
                if image == "":
                    self.controller.aggiungi_cliente(
                        Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, lista_veicoli,
                                username, password, image="Utente/placeholder-user-photo.png"))
                else:
                    self.controller.aggiungi_cliente(
                        Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, lista_veicoli,
                                username, password, image))
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
