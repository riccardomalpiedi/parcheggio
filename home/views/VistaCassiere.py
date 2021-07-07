from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli

class VistaCassiere(QWidget):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        grid_layout = QGridLayout()

        vistalistaveicoli_button = self.create_button("Vista Lista Veicoli", self.go_vista_lista_veicoli)

        grid_layout.addWidget(vistalistaveicoli_button, 0, 0)

        self.setLayout(grid_layout)
        self.resize(500, 400)
        self.setWindowTitle('Vista Cassiere')

        def go_vista_lista_veicoli (self):
            self.vista_lista_veicoli = VistaListaVeicoli
            self.vista_lista_veicoli.show()