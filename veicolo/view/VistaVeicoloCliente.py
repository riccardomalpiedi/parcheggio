from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from prenotazione.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione
from prenotazione.views.VistaPrenotazioneCliente import VistaPrenotazioneCliente
from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloCliente(QDialog):
    def __init__(self, veicolo, elimina_veicolo, prenotazione_callback, callback, parent=None):
        super(VistaVeicoloCliente, self).__init__(parent)
        loadUi("veicolo/view/VistaVeicoloCliente.ui", self)

        self.controller = ControlloreVeicolo(veicolo)
        self.elimina_veicolo = elimina_veicolo
        self.prenotazione_callback = prenotazione_callback
        self.callback = callback
        self.controller.check_prenotazione_scaduta()

        self.targa_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_targa_veicolo())
        self.tipo_label.setText("<font color='white'>Tipo: " + self.controller.get_tipo_veicolo())
        self.visualizza_prenotazione_button.clicked.connect(self.visualizza_prenotazione_click)
        self.nuova_prenotazione_button.clicked.connect(self.nuova_prenotazione_click)
        self.elimina_button.clicked.connect(self.elimina_veicolo_click)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(veicolo.targa)

    def visualizza_prenotazione_click(self):
        if self.controller.get_prenotazione() is not None:
            self.vista_prenotazione = VistaPrenotazioneCliente(self.controller.get_prenotazione(),
                                                               self.controller.elimina_prenotazione)
            self.vista_prenotazione.show()
        else:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non ha alcuna prenotazione",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def nuova_prenotazione_click(self):
        if self.controller.get_prenotazione() is not None:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato ha già una prenotazione",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller)
            self.vista_inserisci_prenotazione.show()

    def elimina_veicolo_click(self):
        if self.controller.get_prenotazione() is not None:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato ha una prenotazione attiva",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.elimina_veicolo(self.controller.get_id_veicolo())
        self.callback()
        self.close()

    def closeEvent(self, event):
        self.prenotazione_callback(self.controller.get_id_veicolo(), self.controller.get_prenotazione())
