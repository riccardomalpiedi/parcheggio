from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from cliente.controller.ControlloreCliente import ControlloreCliente
from cliente.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class ModificaProfilo(QDialog):
    def __init__(self, cliente, elimina_cliente, elimina_callback):
        super(ModificaProfilo, self).__init__()
        loadUi("Utente/Profilo/ModificaProfilo/ModificaProfilo2.ui", self)

        self.cliente = cliente
        self.controller = ControlloreCliente(self.cliente)
        self.controller2 = ControlloreListaClienti()
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback
        # self.callback = callback

        self.nome_field.setText(self.controller.get_nome_cliente())
        self.cognome_field.setText(self.controller.get_cognome_cliente())
        self.cf_field.setText(self.controller.get_cf_cliente())
        self.indirizzo_field.setText(self.controller.get_indirizzo_cliente())
        self.email_field.setText(self.controller.get_email_cliente())
        self.telefono_field.setText(self.controller.get_telefono_cliente())
        # if self.controller.get_veicolo_by_index(0) is not None:
        #    self.veicolo_label.setText(self.controller.get_veicolo_by_index(0).targa)
            # self.tipo_veicolo_label.setText("<font color='white'>Tipo: " + self.controller.get_veicolo_by_index(0).tipo)
        # if self.controller.get_veicolo_by_index(1) is not None:
        #    self.veicolo2_label.setText(self.veicolo2_label.text() + self.controller.get_veicolo_by_index(1).targa)
            # self.tipo_veicolo2_label.setText("<font color='white'>Tipo: " + self.controller.get_veicolo_by_index(1).tipo)
        self.veicolo_field.setText(self.controller.get_veicolo_by_index(0).targa)
        if self.controller.get_veicolo_by_index(1) is not None:
            self.veicolo2_field.setText(self.controller.get_veicolo_by_index(1).targa)
        else:
            self.veicolo2_field.setText(" ")
        self.username_field.setText(self.controller.get_username_cliente())
        self.password_field.setText(self.controller.get_password_cliente())
        self.image_field.setText(self.controller.get_image_cliente())

        self.ok_button.clicked.connect(self.go_modifica_cliente)
        self.back_button.clicked.connect(self.go_back)

    def go_modifica_cliente(self):
        nome = self.nome_field.text()
        cognome = self.cognome_field.text()
        cf = self.cf_field.text()
        indirizzo = self.indirizzo_field.text()
        email = self.email_field.text()
        telefono = self.telefono_field.text()
        veicolo = self.veicolo_field.text()
        veicolo2 = self.veicolo2_field.text()
        username = self.username_field.text()
        password = self.password_field.text()
        image = self.image_field.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" \
                or username == "" or password == "":

            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                  QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.elimina_cliente_click()
            self.controller2.aggiungi_cliente(
                Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, veicolo,
                        veicolo2, username, password, image))
            self.callback()
            self.close()

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()
        # pass

    def go_back(self):
        self.close()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller2.save_data()
        event.accept()
