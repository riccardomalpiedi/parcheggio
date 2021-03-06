from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from home.views.VistaLoginCliente import VistaLoginCliente
from listaveicoli.view.VistaIngressoVeicolo import VistaIngressoVeicolo
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
from listaveicoli.view.VistaUscitaVeicolo import VistaUscitaVeicolo


class VistaHomeCliente(QDialog):
    def __init__(self):
        super(VistaHomeCliente, self).__init__()
        loadUi("home/views/VistaHomeCliente.ui", self)

        self.controller = ControlloreListaClienti()

        self.ingresso_button.clicked.connect(self.go_vista_ingresso)
        self.uscita_button.clicked.connect(self.go_vista_uscita)
        self.accedi_button.clicked.connect(self.go_accedi)
        self.registrati_button.clicked.connect(self.go_registrazione)

        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.setWindowTitle("Cliente")
        self.setWindowIcon(QIcon("icone/user2.png"))

    def go_registrazione(self):
        self.registrazione = VistaInserisciCliente(self.controller)
        self.registrazione.show()
        self.close()

    def go_accedi(self):
        self.accedi = VistaLoginCliente()
        self.accedi.show()
        self.close()

    def go_vista_ingresso(self):
        self.ingresso = VistaIngressoVeicolo()
        self.ingresso.show()

    def go_vista_uscita(self):
        self.uscita = VistaUscitaVeicolo()
        self.uscita.show()
