from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from prenotazione.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione
from prenotazione.views.VistaPrenotazione import VistaPrenotazione
from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicolo(QDialog):
    def __init__(self, veicolo, elimina_veicolo, elimina_callback, parent=None):
        super(VistaVeicolo, self).__init__(parent)
        loadUi("veicolo/view/vistaveicolo.ui", self)

        self.controller = ControlloreVeicolo(veicolo)
        self.elimina_veicolo = elimina_veicolo
        self.elimina_callback = elimina_callback

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
            self.vista_prenotazione = VistaPrenotazione(self.controller.get_prenotazione(),
                                                        self.controller.elimina_prenotazione)
            self.vista_prenotazione.show()
        else:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non ha alcuna prenotazione",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def nuova_prenotazione_click(self):
        if self.controller.get_prenotazione() is None:
            QMessageBox.critical(self, 'Errore', "Il veicolo selezionato ha già una prenotazione",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller)
            self.vista_inserisci_prenotazione.show()

    def elimina_veicolo_click(self):
        self.elimina_veicolo(self.controller.get_id_veicolo())
        self.elimina_callback()
        self.close()
