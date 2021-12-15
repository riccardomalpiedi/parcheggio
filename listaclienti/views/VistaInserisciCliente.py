import os
import random
import shutil

from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.uic import loadUi

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QDialog):
    def __init__(self, controller):
        super(VistaInserisciCliente, self).__init__()
        loadUi("listaclienti/views/VistaInserisciCliente.ui", self)

        self.controller = controller

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
        username = self.username_field.text()
        password = self.password_field.text()
        image = self.immagine_profilo_field.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" \
                or username == "" or password == "":

            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if image == "":
                self.controller.aggiungi_cliente(
                    Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, None,
                                username, password, image="cliente/placeholder-user-photo.png"))
            else:
                self.controller.aggiungi_cliente(
                    Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, None,
                            username, password, image))
            self.close()

    def go_back(self):
        self.close()

    def go_browse(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Images (*.png *.xmp *.jpg)')   # apre l'esplora risorse
        var = fname[0]                           # prende il percorso del file selezionato
        print(var)
        rand = random.randint(1, 2)            # rinomina il file con un numero random
        var2 = "cliente/ImmaginiProfilo/" + str(rand) + ".png"
        print(var2)
        while os.path.isfile(var2):                 # controlla se il file è gia presente
            rand1 = random.randint(451, 1850)
            var2 = "cliente/ImmaginiProfilo/" + str(rand1) + ".png"
            print(var2)
        shutil.copyfile(var, var2)   # copia il file con il nome modificato nell'apposita cartella
        self.immagine_profilo_field.setText(var2)

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
