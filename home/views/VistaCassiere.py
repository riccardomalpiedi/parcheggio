from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.uic import loadUi

from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli


class VistaCassiere(QDialog):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        loadUi("Cassiere.ui", self)
        self.setWindowTitle('Vista Cassiere')
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/cash2.png"))
        self.lista_veicoli_button.clicked.connect(self.go_vista_lista_veicoli)
        self.back_button.clicked.connect(self.go_back)

    def go_vista_lista_veicoli(self):
        self.vista_lista_veicoli = VistaListaVeicoli()
        self.vista_lista_veicoli.show()

    def go_back(self):
        self.close()
