import os
import pickle
from datetime import datetime

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo


class VistaIngressoVeicolo(QWidget):
    def __init__(self):
        super(VistaIngressoVeicolo, self).__init__()
        loadUi("listaveicoli/view/VistaIngressoVeicolo.ui", self)

        self.controller = ControlloreListaVeicoli()
        self.update_ui()

        self.pushButton.clicked.connect(self.go_vista_inserisci_veicolo)
        self.entra_button.clicked.connect(self.inserisci_ingresso_veicolo)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Ingresso Parcheggio")

    def update_ui(self):
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

    def go_vista_inserisci_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.update_ui)
        self.vista_inserisci_veicolo.show()

    def inserisci_ingresso_veicolo(self):
        targa = self.comboBox.currentText()
        veicolo = self.controller.get_veicolo_by_targa(targa)
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                lista_posteggi_salvata = pickle.load(f)
        if veicolo.orario_ingresso is not None:
            QMessageBox.critical(self, 'Errore', "Il veicolo si trova già nel parcheggio",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if veicolo.prenotazione is not None:
                veicolo.check_prenotazione_scaduta()
            if veicolo.prenotazione is not None and veicolo.prenotazione.data_inizio < datetime.now():
                reply = QMessageBox.question(self, "Attenzione", "Il veicolo ha una prenotazione per il " +
                                             veicolo.prenotazione.posteggio.nome +
                                             ": confermare l'ingresso?", QMessageBox.Ok, QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    veicolo.entrato_con_prenotazione = True
                    veicolo.posteggio_occupato = veicolo.prenotazione.posteggio
                    self.ingresso_function(veicolo, lista_posteggi_salvata, veicolo.posteggio_occupato)
            # Ingresso di un veicolo senza prenotazione
            else:
                for posteggio in lista_posteggi_salvata:
                    if veicolo.tipo == posteggio.tipo and posteggio.is_disponibile():
                        posteggio.disponibile = False
                        veicolo.posteggio_occupato = posteggio
                        self.ingresso_function(veicolo, lista_posteggi_salvata, posteggio)
                        return
                QMessageBox.critical(self, 'Errore', "Ci dispiace, non ci sono posti disponibili",
                                     QMessageBox.Ok, QMessageBox.Ok)

    def ingresso_function(self, veicolo, lista_posteggi_salvata, posteggio):
        veicolo.set_orario_ingresso(datetime.now())
        with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as f:
            pickle.dump(lista_posteggi_salvata, f, pickle.HIGHEST_PROTOCOL)
        QMessageBox.information(self, "Operazione riuscita", "Benvenuto nel nostro parcheggio, può accomodarsi al " +
                                posteggio.nome)
        self.close()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
