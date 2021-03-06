from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.uic import loadUi


from home.views.ModificaPassword import ModificaPassword
from listaveicoli.view.VistaListaVeicoliCassiere import VistaListaVeicoliCassiere


class VistaCassiere(QDialog):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        loadUi("home/views/VistaCassiere.ui", self)

        self.lista_veicoli_button.clicked.connect(self.go_vista_lista_veicoli)
        self.modifica_password_button.clicked.connect(self.go_modifica_password)

        self.setWindowTitle('Vista Cassiere')
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/cash2.png"))

    def go_vista_lista_veicoli(self):
        self.vista_lista_veicoli = VistaListaVeicoliCassiere()
        self.vista_lista_veicoli.show()

    def go_modifica_password(self):
        self.modifica_password = ModificaPassword("Cassiere")
        self.modifica_password.show()
