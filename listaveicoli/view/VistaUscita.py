import os
import pickle
from datetime import datetime, timedelta

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli


class VistaUscita(QWidget):
    def __init__(self):
        super(VistaUscita, self).__init__()
        loadUi("listaveicoli/view/VistaUscita.ui", self)

        self.controller = ControlloreListaVeicoli()

        self.comboveicoli_model = QStandardItemModel(self.comboBox)
        for veicolo in self.controller.get_lista_dei_veicoli():
            item = QStandardItem()
            item.setText(veicolo.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboveicoli_model.appendRow(item)
        self.comboBox.setModel(self.comboveicoli_model)

        self.esci_button.clicked.connect(self.inserisci_uscita_veicolo)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Uscita Parcheggio")

    def inserisci_uscita_veicolo(self):
        targa = self.comboBox.currentText()
        veicolo = self.controller.get_veicolo_by_targa(targa)
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                lista_posteggi_salvata = pickle.load(f)
        if veicolo.orario_ingresso is None:
            QMessageBox.critical(self, 'Errore', "Il veicolo non si trova nel parcheggio",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if veicolo.entrato_con_prenotazione and veicolo.get_prenotazione().pagata and \
                                     not veicolo.get_prenotazione().is_scaduta():
                veicolo.entrato_con_prenotazione = False
                self.uscita_function(veicolo, lista_posteggi_salvata)
                return
            if veicolo.orario_pagato is None or datetime.now() - veicolo.orario_pagato > timedelta(minutes=15):
                QMessageBox.critical(self, 'Errore', "Prima di uscire deve effettuare il pagamento alla cassa",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                for posteggio in lista_posteggi_salvata:
                    if veicolo.posteggio_occupato.id == posteggio.id:
                        posteggio.disponibile = True
                        veicolo.posteggio_occupato = None
                        self.uscita_function(veicolo, lista_posteggi_salvata)
                        return

    def uscita_function(self, veicolo, lista_posteggi_salvata):
        veicolo.set_orario_ingresso(None)
        veicolo.set_orario_pagato(None)
        with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as f:
            pickle.dump(lista_posteggi_salvata, f, pickle.HIGHEST_PROTOCOL)
        QMessageBox.information(self, "Operazione riuscita", "Può uscire dal parcheggio")
        self.close()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
