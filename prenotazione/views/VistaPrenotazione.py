import os
import pickle

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
        self.data_inizio_label.setText("<font color='white'>Inizio: " +
                                       self.controller.get_data_inizio_prenotazione().strftime("%d:%m:%Y"))
        self.data_fine_label.setText("<font color='white'>Fine: " +
                                     self.controller.get_data_fine_prenotazione().strftime("%d:%m:%Y"))

        self.disdici_button.clicked.connect(self.disdici_prenotazione_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def disdici_prenotazione_click(self):
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                lista_posteggi_salvata = pickle.load(f)
        for posteggio in lista_posteggi_salvata:
            if posteggio.id == self.controller.get_posteggio_prenotazione().id:
                posteggio.disponibile = True
        with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as f:
            pickle.dump(lista_posteggi_salvata, f, pickle.HIGHEST_PROTOCOL)
        self.disdisci_prenotazione()
        self.close()
