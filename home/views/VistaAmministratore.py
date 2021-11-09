from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from home.views.ModificaPasswordAmmeCas import ModificaPasswordAmmeCas
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaposteggi.views.VistaListaPosteggi import VistaListaPosteggi
from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli


class VistaAmministratore(QDialog):
    def __init__(self):
        super(VistaAmministratore, self).__init__()
        loadUi("Amministratore2.ui", self)

        self.setWindowTitle("Amministratore")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/administrator2.png"))

        self.vista_lista_clienti_button.clicked.connect(self.go_lista_vista_clienti)
        self.vista_lista_posteggi_button.clicked.connect(self.go_lista_vista_posteggi)
        self.vista_lista_veicoli_button.clicked.connect(self.go_lista_vista_veicoli)
        self.vista_lista_dipendenti_button.clicked.connect(self.go_lista_vista_dipendenti)
        self.modifica_password_button.clicked.connect(self.go_modifica_password)
        self.back_button.clicked.connect(self.go_back_button)

    def go_lista_vista_clienti(self):
        self.lista_vista_clienti = VistaListaClienti()
        self.lista_vista_clienti.show()

    def go_lista_vista_posteggi(self):
        self.lista_vista_posteggi = VistaListaPosteggi()
        self.lista_vista_posteggi.show()

    def go_lista_vista_veicoli(self):
        self.lista_vista_veicoli = VistaListaVeicoli()
        self.lista_vista_veicoli.show()

    def go_lista_vista_dipendenti(self):
        self.lista_vista_dipendenti = VistaListaDipendenti()
        self.lista_vista_dipendenti.show()

    def go_modifica_password(self):
        self.modifica_password = ModificaPasswordAmmeCas("Amministratore")
        self.modifica_password.show()

    def go_back_button(self):
        self.close()
