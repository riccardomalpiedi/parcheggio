import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        loadUi("NuovaPrenotazione.ui", self)

        self.controller = controller
        self.callback = callback

        self.data_inizio_lineEdit.text()
        self.data_fine_lineEdit.text()

        self.comboclienti_model = QStandardItemModel(self.cliente_comboBox)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)
            for cliente in self.lista_clienti_salvata:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.cliente_comboBox.setModel(self.comboclienti_model)

        self.comboposteggi_model = QStandardItemModel(self.posteggio_comboBox)
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                self.lista_posteggi_salvata = pickle.load(f)
            self.lista_posteggi_disponibili = [s for s in self.lista_posteggi_salvata if s.is_disponibile()]
            for posteggio in self.lista_posteggi_disponibili:
                item = QStandardItem()
                item.setText(posteggio.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboposteggi_model.appendRow(item)
            self.posteggio_comboBox.setModel(self.comboposteggi_model)

        self.comboveicoli_model = QStandardItemModel(self.veicolo_comboBox)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                self.lista_veicoli_salvata = pickle.load(f)
            for veicolo in self.lista_veicoli_salvata:
                item = QStandardItem()
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboveicoli_model.appendRow(item)
            self.veicolo_comboBox.setModel(self.comboveicoli_model)

        self.ok_button.clicked.connect(self.add_prenotazione)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Prenotazione')
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def add_prenotazione(self):
        data_inizio = self.data_inizio_lineEdit.text()
        data_fine = self.data_fine_lineEdit.text()
        cliente = self.lista_clienti_salvata[self.cliente_comboBox.currentIndex()]
        posteggio = self.lista_posteggi_disponibili[self.posteggio_comboBox.currentIndex()]
        veicolo = self.lista_veicoli_salvata[self.veicolo_comboBox.currentIndex()]
        if data_inizio == "" or not cliente or not posteggio:
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((cliente.cognome + posteggio.nome).lower(), cliente, veicolo, posteggio, data_inizio, data_fine))
            posteggio.prenota()
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_posteggi_salvata, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()