from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QDialog):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        loadUi("VistaPrenotazione.ui", self)

        self.controller = ControllorePrenotazione(prenotazione)
        self.disdisci_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        self.posto_label.setText("<font color='white'>" + self.controller.get_posteggio_prenotazione().nome)
        self.cliente_label.setText("<font color='white'>Cliente: " +
                                   self.controller.get_cliente_prenotazione().nome + " " +
                                   self.controller.get_cliente_prenotazione().cognome)
        self.data_inizio_label.setText("<font color='white'>Inizio: " + self.controller.get_data_inizio_prenotazione())
        self.data_fine_label.setText("<font color='white'>Fine: " + self.controller.get_data_fine_prenotazione())

        self.disdici_button.clicked.connect(self.disdici_prenotazione_click)

        self.setFixedHeight(363)
        self.setFixedWidth(357)
        self.setWindowTitle(self.controller.get_cliente_prenotazione().nome)
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def disdici_prenotazione_click(self):
        self.disdisci_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()