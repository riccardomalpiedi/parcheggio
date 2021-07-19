from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from ingresso.views.VistaIngresso import VistaIngresso
from uscita.views.VistaUscita import VistaUscita


class VistaUtente(QDialog):
    def __init__(self):
        super(VistaUtente, self).__init__()
        loadUi("Utente/Cliente.ui", self)

        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.setWindowTitle("Cliente")
        self.setWindowIcon(QIcon("icone/user2.png"))

        self.ingresso_button.clicked.connect(self.go_vista_ingresso)
        self.uscita_button.clicked.connect(self.go_vista_uscita)

    def go_vista_ingresso(self):
        self.ingresso = VistaIngresso()
        self.ingresso.show()

    def go_vista_uscita(self):
        self.uscita = VistaUscita()
        self.uscita.show()
