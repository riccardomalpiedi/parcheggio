
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from cliente.view.VistaProfiloCliente import VistaProfiloCliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaLoginCliente(QDialog):
    def __init__(self):
        super(VistaLoginCliente, self).__init__()
        loadUi("home/views/VistaLoginCliente.ui", self)

        self.controller = ControlloreListaClienti()

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_function)
        self.back_button.clicked.connect(self.back_function)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Login")

    def login_function(self):
        user = self.username_field.text()
        password = self.password_field.text()

        if user == "" and password == "" or len(user) == 0 or len(password) == 0:
            QMessageBox.critical(self, "Errore", "Inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            for cliente in self.controller.get_lista_dei_clienti():
                if user == cliente.username:
                    if password == cliente.password:
                        self.go_vista_profilo_cliente(cliente)
                        return
        QMessageBox.critical(self, 'Errore', "Credenziali errate", QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_profilo_cliente(self, cliente):
        self.vista_profilo_cliente = VistaProfiloCliente(cliente, self.update_list, self.controller.elimina_cliente_by_id)
        self.vista_profilo_cliente.show()
        self.close()

    def update_list(self):
        self.controller.save_data()

    def back_function(self):
        self.close()
