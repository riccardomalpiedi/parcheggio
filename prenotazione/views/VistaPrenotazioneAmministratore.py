from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazioneAmministratore(QDialog):
    def __init__(self, prenotazione, parent=None):
        super(VistaPrenotazioneAmministratore, self).__init__(parent)
        loadUi("prenotazione/views/VistaPrenotazioneAmministratore.ui", self)

        self.controller = ControllorePrenotazione(prenotazione)

        self.posto_label.setText("<font color='white'>" + self.controller.get_posteggio_prenotazione().nome)
        self.data_inizio_label.setText("<font color='white'>Inizio: " + self.controller.get_data_inizio_prenotazione().
                                       strftime("%d:%m:%Y"))
        self.data_fine_label.setText("<font color='white'>Fine: " + self.controller.get_data_fine_prenotazione().
                                     strftime("%d:%m:%Y"))

        self.ok_button.clicked.connect(self.ok)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def ok(self):
        self.close()
