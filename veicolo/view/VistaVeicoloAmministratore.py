from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from prenotazione.views.VistaPrenotazioneAmministratore import VistaPrenotazioneAmministratore
from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloAmministratore(QDialog):
    def __init__(self, veicolo, parent=None):
        super(VistaVeicoloAmministratore, self).__init__(parent)
        loadUi("veicolo/view/vistaveicoloAmministratore.ui", self)

        self.controller = ControlloreVeicolo(veicolo)

        self.targa_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_targa_veicolo())
        self.tipo_label.setText("<font color='white'>Tipo: " + self.controller.get_tipo_veicolo())
        self.visualizza_prenotazione_button.clicked.connect(self.visualizza_prenotazione_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(veicolo.targa)

    def visualizza_prenotazione_click(self):
        if self.controller.get_prenotazione() is not None:
            self.vista_prenotazione = VistaPrenotazioneAmministratore(self.controller.get_prenotazione())
            self.vista_prenotazione.show()
        else:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non ha alcuna prenotazione",
                                 QMessageBox.Ok, QMessageBox.Ok)
