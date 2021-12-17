from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from cliente.controller.ControlloreCliente import ControlloreCliente


# Vista del cliente accedibile dall'amministratore. Sono solo riportate le informazioni del cliente
class VistaCliente(QDialog):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__(parent)
        loadUi("cliente/view/vistacliente.ui", self)

        self.controller = ControlloreCliente(cliente)

        self.nome_label.setText("<font color='white'>" + self.controller.get_nome_cliente() + " " +
                                self.controller.get_cognome_cliente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_cliente())
        self.indirizzo_label.setText("<font color='white'>Indirizzo: " + self.controller.get_indirizzo_cliente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_cliente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_cliente())
        if self.controller.get_lista_dei_veicoli() is None or len(self.controller.get_lista_dei_veicoli()) == 0:
            self.targa_veicolo_label.setText("<font color='white'>Nessun veicolo associato")
        else:
            self.targa_veicolo_label.setText("<font color='white'>Targa Veicolo: " +
                                             self.controller.get_veicolo_by_index(0).targa)
            if len(self.controller.get_lista_dei_veicoli()) > 1:
                self.targa_veicolo2_label.setText(" <font color='white'>Targa Veicolo2: " +
                                                  self.controller.get_veicolo_by_index(1).targa)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(cliente.nome)
        self.setWindowIcon(QIcon("icone/user2.png"))
