from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Login.LoginCliente import LoginCliente
from ingresso.views.VistaIngresso import VistaIngresso
from uscita.views.VistaUscita import VistaUscita


class VistaHomeCliente(QDialog):
    def __init__(self):
        super(VistaHomeCliente, self).__init__()
        loadUi("home/BenvenutoCliente2.ui", self)

        self.setFixedWidth(632)
        self.setFixedHeight(451)
        self.setWindowTitle("Cliente")
        self.setWindowIcon(QIcon("icone/user2.png"))
        self.ingresso_button.clicked.connect(self.go_vista_ingresso)
        self.uscita_button.clicked.connect(self.go_vista_uscita)
        self.accedi_button.clicked.connect(self.go_accedi)

    def go_accedi(self):
        self.accedi = LoginCliente()
        self.accedi.show()
        self.close()

    def go_vista_ingresso(self):
        self.ingresso = VistaIngresso()
        self.ingresso.show()

    def go_vista_uscita(self):
        self.uscita = VistaUscita()
        self.uscita.show()
