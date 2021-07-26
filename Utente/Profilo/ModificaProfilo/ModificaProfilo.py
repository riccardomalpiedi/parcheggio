from PyQt5.QtWidgets import QGridLayout, QWidget, QDialog, QMessageBox
# from PyQt5.uic import loadUi

# # from cliente.controller.ControlloreCliente import ControlloreCliente
# from cliente.model.Cliente import Cliente
# # from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti

class ModificaProfilo(QWidget):
    def __init__(self):
        super(ModificaProfilo, self).__init__()
        grid_layout = QGridLayout()
    #     loadUi("Utente/Profilo/ModificaProfilo/ModificaProfilo.ui", self)
    #
    #     self.cliente = cliente
    #     self.callback = callback
    #     self.controller1 = controller1
    #
    #     self.ok_button.clicked.connect(self.go_modifica_cliente)
    #     self.back_button.clicked.connect(self.go_back)
    #
    # def go_modifica_cliente(self):
    #     nome = self.nome_field.text()
    #     cognome = self.nome_field.text()
    #     cf = self.nome_field.text()
    #     indirizzo = self.nome_field.text()
    #     email = self.email_field.text()
    #     telefono = self.nome_field.text()
    #     veicolo = self.nome_field.text()
    #     username = self.nome_field.text()
    #     password = self.nome_field.text()
    #     image = self.nome_field.text()
    #
    #     if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or veicolo == "" \
    #             or username == "" or password == "":
    #
    #         QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
    #                              QMessageBox.Ok, QMessageBox.Ok)
    #     else:
    #         self.elimina_cliente_click()
    #         self.controller1.aggiungi_cliente(
    #             Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, veicolo, username,
    #                     password, image))
    #         self.callback()
    #         self.close()
    #
    # def elimina_cliente_click(self):
    #     self.elimina_cliente(self.controller.get_id_cliente())
    #     self.elimina_callback()
    #     return
    #     # self.close()
    #
    # def go_back(self):
    #     self.close()
    #
    # def closeEvent(self, event):
    #     print("ON CLOSE")
    #     self.controller1.save_data()
    #     event.accept()
