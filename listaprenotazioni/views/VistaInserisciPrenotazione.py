import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QComboBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()

        v_layout.addWidget(QLabel("Data di inizio (dd/MM/yyyy)"))
        self.text_datainizio = QLineEdit(self)
        v_layout.addWidget(self.text_datainizio)

        v_layout.addWidget(QLabel("Data di fine (dd/MM/yyyy)"))
        self.text_datafine = QLineEdit(self)
        v_layout.addWidget(self.text_datafine)

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
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
            self.combo_clienti.setModel(self.comboclienti_model)
        v_layout.addWidget(QLabel("Cliente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_posteggi = QComboBox()
        self.comboposteggi_model = QStandardItemModel(self.combo_posteggi)
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
            self.combo_posteggi.setModel(self.comboposteggi_model)
        v_layout.addWidget(QLabel("Posteggio"))
        v_layout.addWidget(self.combo_posteggi)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Prenotazione')

    def add_prenotazione(self):
        data_inizio = self.text_datainizio.text()
        data_fine = self.text_datafine.text()
        cliente = self.lista_clienti_salvata[self.combo_clienti.currentIndex()]
        posteggio = self.lista_posteggi_disponibili[self.combo_posteggi.currentIndex()]
        if data_inizio == "" or not cliente or not posteggio:
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((cliente.cognome+posteggio.nome).lower(), cliente, posteggio, data_inizio, data_fine))
            posteggio.prenota()
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_posteggi_salvata, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()