from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from abbonamento.view.VistaAbbonamento import VistaAbbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaCliente(QDialog):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        loadUi("vistacliente.ui", self)

        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback

        self.nome_label.setText("<font color='white'>" + self.controller.get_nome_cliente() + " " +
                                self.controller.get_cognome_cliente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_cliente())
        self.indirizzo_label.setText("<font color='white'>Indirizzo: " + self.controller.get_indirizzo_cliente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_cliente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_cliente())
        self.targa_veicolo_label.setText("<font color='white'>Targa Veicolo: " +
                                         self.controller.get_veicolo_cliente().targa + "" +
                                         self.controller.get_veicolo2_cliente().targa)

        self.abbonamento_button.clicked.connect(self.check_abbonamento)
        self.elimina_button.clicked.connect(self.elimina_cliente_click)

        self.setFixedHeight(543)
        self.setFixedWidth(357)
        self.setWindowTitle(cliente.nome)
        self.setWindowIcon(QIcon("icone/user2.png"))

    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(),
                                                  self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()