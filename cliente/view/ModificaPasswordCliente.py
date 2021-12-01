from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets


class ModificaPasswordCliente(QDialog):
    def __init__(self, controller):
        super(ModificaPasswordCliente, self).__init__()
        loadUi("cliente/view/ModificaPassword.ui", self)

        self.controller = controller

        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.save_button.clicked.connect(self.modifica_password)
        self.annulla_button.clicked.connect(self.annulla_function)

        self.setWindowTitle("Modifica Password")
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def modifica_password(self):
        nuova_password = self.password_lineEdit.text()
        conferma_password = self.confirm_password_lineEdit.text()

        old_password = self.controller.get_password_cliente()

        if nuova_password == "" or conferma_password == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if nuova_password == old_password:
                QMessageBox.critical(self, 'Errore', "Passwrod uguale a quella gia inserita in passato!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                if nuova_password == conferma_password:
                    self.controller.set_password_cliente(nuova_password)
                    self.close()
                else:
                    QMessageBox.critical(self, 'Errore', "Le due password non coincidono, ricontrolla!",
                                         QMessageBox.Ok, QMessageBox.Ok)

    def annulla_function(self):
        self.close()
