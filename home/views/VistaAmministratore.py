from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from home.views.ModificaPassword import ModificaPassword
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaposteggi.views.VistaListaPosteggi import VistaListaPosteggi
from listaveicoli.view.VistaListaVeicoliAmministratore import VistaListaVeicoliAmministratore


class VistaAmministratore(QDialog):
    def __init__(self):
        super(VistaAmministratore, self).__init__()
        loadUi("home/views/VistaAmministratore.ui", self)

        self.setWindowTitle("Amministratore")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/administrator2.png"))

        self.vista_lista_clienti_button.clicked.connect(self.go_vista_lista_clienti)
        self.vista_lista_posteggi_button.clicked.connect(self.go_vista_lista_posteggi)
        self.vista_lista_veicoli_button.clicked.connect(self.go_vista_lista_veicoli)
        self.vista_lista_dipendenti_button.clicked.connect(self.go_vista_lista_dipendenti)
        self.modifica_password_button.clicked.connect(self.go_modifica_password)
        self.back_button.clicked.connect(self.go_back_button)

    def go_vista_lista_clienti(self):
        self.lista_vista_clienti = VistaListaClienti()
        self.lista_vista_clienti.show()

    def go_vista_lista_posteggi(self):
        self.lista_vista_posteggi = VistaListaPosteggi()
        self.lista_vista_posteggi.show()

    def go_vista_lista_veicoli(self):
        self.lista_vista_veicoli = VistaListaVeicoliAmministratore()
        self.lista_vista_veicoli.show()

    def go_vista_lista_dipendenti(self):
        self.lista_vista_dipendenti = VistaListaDipendenti()
        self.lista_vista_dipendenti.show()

    def go_modifica_password(self):
        self.modifica_password = ModificaPassword("Amministratore")
        self.modifica_password.show()

    def go_back_button(self):
        self.close()
