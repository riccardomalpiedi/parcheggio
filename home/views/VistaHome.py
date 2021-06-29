from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from home.views.VistaAmministratore import VistaAmministratore
from home.views.VistaCassiere import VistaCassiere
from home.views.VistaCliente import VistaCliente


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        cassiere_button = self.create_button("Vista Cassiere", "icone/cash2.png", self.go_vista_cassiere)
        cliente_button = self.create_button("Vista Cliente", "icone/user2.png", self.go_vista_cliente)
        amministratore_button = self.create_button("Vista Amministratore",
                                                   "icone/administrator2.png", self.go_vista_amministratore)

        grid_layout.addWidget(cassiere_button, 0, 0)
        grid_layout.addWidget(cliente_button, 0, 1)
        grid_layout.addWidget(amministratore_button, 1, 0)
        self.setLayout(grid_layout)
        self.resize(500, 400)
        self.setWindowTitle('Gestore Parcheggio')

    def create_button(self, titolo, icona, on_click=None):
        button = QPushButton(titolo)
        button.setFont(QFont("arial", 12))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setIcon(QIcon(icona))
        return button

    def go_vista_cassiere(self):
        self.vista_cassiere = VistaCassiere()
        self.vista_cassiere.show()

    def go_vista_cliente(self):
        self.vista_cliente = VistaCliente()
        self.vista_cliente.show()

    def go_vista_amministratore(self):
        self.vista_amministratore = VistaAmministratore()
        self.vista_amministratore.show()