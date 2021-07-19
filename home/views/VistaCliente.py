from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Login.LoginCliente import LoginCliente
from Login.RegistrazioneNuovoCliente import RegistrazioneNuovoCliente
# from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
# from listaclienti.views.VistaListaClienti import VistaListaClienti


class VistaCliente(QDialog):
    def __init__(self):
        super(VistaCliente, self).__init__()
        # self.vista_lista_clienti = VistaListaClienti()
        loadUi("home/BenvenutoCliente.ui", self)

        self.setFixedWidth(632)
        self.setFixedHeight(451)
        self.setWindowTitle("Cliente")
        self.setWindowIcon(QIcon("icone/user2.png"))
        self.registrati_button.clicked.connect(self.go_registrati)
        self.accedi_button.clicked.connect(self.go_accedi)

    def go_accedi(self):
        self.accedi = LoginCliente()
        self.accedi.show()
        self.close()

    def go_registrati(self):
        self.registrati = RegistrazioneNuovoCliente()
        # self.registrati = VistaInserisciCliente(self.vista_lista_clienti.controller, self.vista_lista_clienti.update_ui)
        self.registrati.show()
        self.close()