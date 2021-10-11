from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloAmministratore(QDialog):
    def __init__(self, veicolo, parent=None):
        super(VistaVeicoloAmministratore, self).__init__(parent)
        loadUi("veicolo/view/vistaveicoloAmministratore.ui", self)

        self.controller = ControlloreVeicolo(veicolo)

        self.targa_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_targa_veicolo())
        self.tipo_label.setText("<font color='white'>Tipo: " + self.controller.get_tipo_veicolo())

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(veicolo.targa)
