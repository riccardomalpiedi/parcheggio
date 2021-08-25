from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloDipendente(QDialog):
    def __init__(self, veicolo, elimina_veicolo, elimina_callback, parent=None):
        super(VistaVeicoloDipendente, self).__init__(parent)
        loadUi("vistaveicoloDipendente.ui", self)

        self.controller = ControlloreVeicolo(veicolo)
        self.elimina_veicolo = elimina_veicolo
        self.elimina_callback = elimina_callback

        self.targa_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_targa_veicolo())
        self.tipo_label.setText("<font color='white'>Tipo: " + self.controller.get_tipo_veicolo())
        self.conferma_pagamento_button.clicked.connect(self.pagamento_veicolo_click)
        self.elimina_button.clicked.connect(self.elimina_veicolo_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(veicolo.targa)

    def elimina_veicolo_click(self):
        self.elimina_veicolo(self.controller.get_id_veicolo())
        self.elimina_callback()
        self.close()

    def pagamento_veicolo_click(self):
        self.set_pagato(self, True)
