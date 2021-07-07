from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy

from abbonamento.view.VistaAbbonamento import VistaAbbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf = QLabel("Codice Fiscale: {}".format(self.controller.get_cf_cliente()))
        font_cf = label_cf.font()
        font_cf.setPointSize(17)
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_indirizzo_cliente()))
        font_indirizzo = label_indirizzo.font()
        font_indirizzo.setPointSize(17)
        label_indirizzo.setFont(font_indirizzo)
        v_layout.addWidget(label_indirizzo)

        label_email = QLabel("Email: {}".format(self.controller.get_email_cliente()))
        font_email = label_email.font()
        font_email.setPointSize(17)
        label_email.setFont(font_email)
        v_layout.addWidget(label_email)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_telefono_cliente()))
        font_telefono = label_telefono.font()
        font_telefono.setPointSize(17)
        label_telefono.setFont(font_telefono)
        v_layout.addWidget(label_telefono)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_abbonamento = QPushButton("Abbonamento")
        btn_abbonamento.clicked.connect(self.check_abbonamento)
        v_layout.addWidget(btn_abbonamento)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(cliente.nome)

    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(), self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()