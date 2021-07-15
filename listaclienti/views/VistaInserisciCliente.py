from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        loadUi("NuovoCliente.ui", self)

        self.controller = controller
        self.callback = callback

        self.ok_button.clicked.connect(self.add_cliente)

        self.setFixedHeight(525)
        self.setFixedWidth(238)
        self.setWindowTitle('Nuovo Cliente')

    def add_cliente(self):
        nome = self.nome_lineEdit.text()
        cognome = self.cognome_lineEdit.text()
        cf = self.codice_fiscale_lineEdit.text()
        indirizzo = self.indirizzo_lineEdit.text()
        email = self.email_lineEdit.text()
        telefono = self.telefono_lineEdit.text()

        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_cliente(
                Cliente((nome + cognome).lower(), nome, cognome, cf, indirizzo, email, telefono))
            self.callback()
            self.close()