import os
import random
import shutil

from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.uic import loadUi

# Vista che consente al cliente di modificare le informazioni del proprio profilo.
class ModificaProfiloCliente(QDialog):
    def __init__(self, controller, callback):
        super(ModificaProfiloCliente, self).__init__()
        loadUi("cliente/view/ModificaProfiloCliente.ui", self)

        self.controller = controller
        self.callback = callback

        self.nome_field.setText(self.controller.get_nome_cliente())
        self.cognome_field.setText(self.controller.get_cognome_cliente())
        self.cf_field.setText(self.controller.get_cf_cliente())
        self.indirizzo_field.setText(self.controller.get_indirizzo_cliente())
        self.email_field.setText(self.controller.get_email_cliente())
        self.telefono_field.setText(self.controller.get_telefono_cliente())
        self.image_label.setText(self.controller.get_image_cliente())

        self.save_button.clicked.connect(self.modifica_profilo)
        self.browse_button.clicked.connect(self.go_cambia_immagine)
        self.back_button.clicked.connect(self.go_back)

        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def modifica_profilo(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.cf_field.text()
        indirizzo = self.indirizzo_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        image = self.image_label.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                  QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.set_nome_cliente(nome)
            self.controller.set_cognome_cliente(cognome)
            self.controller.set_cf_cliente(cf)
            self.controller.set_indirizzo_cliente(indirizzo)
            self.controller.set_email_cliente(email)
            self.controller.set_telefono_cliente(telefono)
            self.controller.set_image_cliente(image)
            self.callback()
            self.close()

    # metodo che consente al cliente di cambiare la propria immagine
    def go_cambia_immagine(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Images (*.png *.xmp *.jpg)')
        var = fname[0]
        print(var)
        if self.controller.get_image_cliente() == "cliente/placeholder-user-photo.png":
            rand = random.randint(851, 900)
            var2 = "cliente/ImmaginiProfilo/" + str(rand) + ".png"
            print(var2)
            while os.path.isfile(var2):  # controlla se il file è gia presente
                rand1 = random.randint(851, 10000)
                var2 = "cliente/ImmaginiProfilo/" + str(rand1) + ".png"
            shutil.copyfile(var, var2)
            print(var2)
            self.image_label.setText(var2)
        else:
            var2 = self.controller.get_image_cliente()
            shutil.copyfile(var, var2)
            print(var2)
            self.image_label.setText(var2)

    def go_back(self):
        self.close()
