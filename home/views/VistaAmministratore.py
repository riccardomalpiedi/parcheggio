from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaposteggi.views.VistaListaPosteggi import VistaListaPosteggi
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli


class VistaAmministratore(QWidget):
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        grid_layout = QGridLayout()

        vistalistaclienti_button = self.create_button("Vista Lista Clienti", "icone/cash2.png", self.go_vista_lista_clienti)
        vistalistadipendenti_button = self.create_button("Vista Lista Dipendenti", "icone/user2.png", self.go_vista_lista_dipendenti)
        vistalistaposteggi_button = self.create_button("Vista Lista Posteggi", "icone/administrator2.png", self.go_vista_lista_posteggi)
        vistalistaprenotazioni_button = self.create_button("Vista Lista Prenotazioni", "icone/cash2.png", self.go_vista_lista_prenotazioni)
        vistalistaveicoli_button = self.create_button("Vista Lista Veicoli", "icone/cash2.png", self.go_vista_lista_veicoli)

        grid_layout.addWidget(vistalistaclienti_button, 0, 0)
        grid_layout.addWidget(vistalistadipendenti_button, 0, 1)
        grid_layout.addWidget(vistalistaposteggi_button, 1, 0)
        grid_layout.addWidget(vistalistaprenotazioni_button, 1, 1)
        grid_layout.addWidget(vistalistaveicoli_button, 2, 0)
        self.setLayout(grid_layout)
        self.resize(500, 400)
        self.setWindowTitle('Vista Amministratore')

    def create_button(self, titolo, icona, on_click=None):
        button = QPushButton(titolo)
        button.setFont(QFont("arial", 12))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        # button.setIcon(QIcon(icona))
        return button

    def go_vista_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_vista_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_vista_lista_posteggi(self):
        self.vista_lista_posteggi = VistaListaPosteggi()
        self.vista_lista_posteggi.show()

    def go_vista_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_vista_lista_veicoli(self):
        self.vista_lista_veicoli = VistaListaVeicoli()
        self.vista_lista_veicoli.show()