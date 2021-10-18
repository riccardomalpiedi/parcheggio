from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QDialog):
    def __init__(self, prenotazione, disdici_prenotazione, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        loadUi("VistaPrenotazione.ui", self)

        self.controller = ControllorePrenotazione(prenotazione)
        self.disdisci_prenotazione = disdici_prenotazione

        self.posto_label.setText("<font color='white'>" + self.controller.get_posteggio_prenotazione().nome)
        self.data_inizio_label.setText("<font color='white'>Inizio: " + self.controller.get_data_inizio_prenotazione())
        self.data_fine_label.setText("<font color='white'>Fine: " + self.controller.get_data_fine_prenotazione())

        self.disdici_button.clicked.connect(self.disdici_prenotazione_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def disdici_prenotazione_click(self):
        self.disdisci_prenotazione()
        self.elimina_callback()
        self.close()
