

from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from datetime import datetime, timedelta

from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicoloCassiere(QDialog):
    def __init__(self, veicolo, parent=None):
        super(VistaVeicoloCassiere, self).__init__(parent)
        loadUi("vistaveicoloDipendente.ui", self)

        self.controller = ControlloreVeicolo(veicolo)
        self.controller.check_prenotazione_scaduta()

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
        # gestione del pagamento di una prenotazione
        elif self.controller.get_entrato_con_prenotazione():
            importo = 0
            if not self.controller.get_prenotazione().pagata:
                importo += (self.controller.get_prenotazione().data_fine -
                             self.controller.get_prenotazione().data_inizio).days * \
                           int(self.controller.get_prenotazione().posteggio.tariffa_giornaliera_prenotazioni)
            if self.controller.get_prenotazione().is_scaduta():
                importo += (datetime.now() - self.controller.get_prenotazione().data_fine).hour *\
                           int(self.controller.get_prenotazione().posteggio.tariffa_oraria)
            if importo == 0:
                QMessageBox.critical(self, 'Errore', "Il pagamento è già stato effettuato", QMessageBox.Ok,
                                     QMessageBox.Ok)
                self.close()
                return
            reply = QMessageBox.question(self, "Attenzione", "L'importo è pari a " + str(importo) +
                                         ": confermare il pagamento?", QMessageBox.Ok, QMessageBox.Cancel)
            if reply == QMessageBox.Ok:
                self.controller.set_orario_pagato(datetime.now())
                self.controller.get_prenotazione().pagata = True
                self.close()
        # gestione pagamento senza prenotazione
        else:
            if self.controller.get_orario_pagato_veicolo() is not None and \
                    datetime.now() - self.controller.get_orario_pagato_veicolo() < timedelta(minutes=15):
                QMessageBox.critical(self, 'Errore', "Il pagamento è già stato effettuato",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                print((datetime.now() - self.controller.get_orario_ingresso()).seconds)
                importo = (((datetime.now() - self.controller.get_orario_ingresso()).seconds//3600 + 1) *
                           self.controller.get_posteggio_occupato().tariffa_oraria)
                reply = QMessageBox.question(self, "Attenzione", "L'importo è pari a " + str(importo) +
                                             ": confermare il pagamento?", QMessageBox.Ok, QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    self.controller.set_orario_pagato(datetime.now())
                    self.close()
