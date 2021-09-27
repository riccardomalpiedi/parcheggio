from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from datetime import datetime, timedelta

from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloDipendente(QDialog):
    def __init__(self, veicolo, parent=None):
        super(VistaVeicoloDipendente, self).__init__(parent)
        loadUi("vistaveicoloDipendente.ui", self)

        self.controller = ControlloreVeicolo(veicolo)

        self.targa_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_targa_veicolo())
        self.tipo_label.setText("<font color='white'>Tipo: " + self.controller.get_tipo_veicolo())
        self.conferma_pagamento_button.clicked.connect(self.pagamento_veicolo_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(veicolo.targa)

    def pagamento_veicolo_click(self):
        if self.controller.get_orario_ingresso() is None:
            QMessageBox.critical(self, 'Errore', "Il veicolo non si trova nel parcheggio",
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif self.controller.get_orario_pagato_veicolo() is not None and \
                datetime.now() - self.controller.get_orario_pagato_veicolo() < timedelta(minutes=15):
            QMessageBox.critical(self, 'Errore', "Il pagamento è già stato effettuato", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.set_orario_pagato(datetime.now())
            print(self.controller.get_orario_pagato_veicolo())
