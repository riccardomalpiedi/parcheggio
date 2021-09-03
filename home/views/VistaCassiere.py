from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.uic import loadUi


from VistaDelCassiere.VistaListaVeicoliDip import VistaListaVeicoliDip


class VistaCassiere(QDialog):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        loadUi("Cassiere.ui", self)

        self.lista_veicoli_button.clicked.connect(self.go_vista_lista_veicoli)
        self.back_button.clicked.connect(self.go_back)

        self.setWindowTitle('Vista Cassiere')
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/cash2.png"))

    def go_vista_lista_veicoli(self):
        self.vista_lista_veicoliDip = VistaListaVeicoliDip()
        self.vista_lista_veicoliDip.show()

    def go_back(self):
        self.close()
