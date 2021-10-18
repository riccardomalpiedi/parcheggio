from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class ModificaProfilo(QDialog):
    def __init__(self, controller, callback):
        super(ModificaProfilo, self).__init__()
        loadUi("cliente/view/ModificaProfilo2.ui", self)

        self.controller = controller
        self.callback = callback

        self.nome_field.setText(self.controller.get_nome_cliente())
        self.cognome_field.setText(self.controller.get_cognome_cliente())
        self.cf_field.setText(self.controller.get_cf_cliente())
        self.indirizzo_field.setText(self.controller.get_indirizzo_cliente())
        self.email_field.setText(self.controller.get_email_cliente())
        self.telefono_field.setText(self.controller.get_telefono_cliente())
        self.image_label.setText(self.controller.get_image_cliente())

        self.ok_button.clicked.connect(self.go_modifica_cliente)
        self.back_button.clicked.connect(self.go_back)

        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def go_modifica_cliente(self):
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
            self.callback()
            self.close()

    def go_back(self):
        self.close()
