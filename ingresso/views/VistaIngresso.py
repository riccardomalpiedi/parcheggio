import os
import pickle
from datetime import datetime

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo
from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        self.vista_lista_veicoli = VistaListaVeicoli()
        loadUi("Ingresso.ui", self)

        self.comboveicoli_model = QStandardItemModel(self.comboBox)
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
            self.comboBox.setModel(self.comboveicoli_model)

        self.pushButton.clicked.connect(self.go_vista_inserisci_veicolo)
        self.entra_button.clicked.connect(self.inserisci_ingresso_veicolo)

    def go_vista_inserisci_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.vista_lista_veicoli.controller,
                                                             self.vista_lista_veicoli.update_ui)
        self.vista_inserisci_veicolo.show()

    def inserisci_ingresso_veicolo(self):
        targa = self.comboBox.currentText()
        veicolo = self.vista_lista_veicoli.controller.get_veicolo_by_targa(targa)
        veicolo.set_orario_ingresso(datetime.now())
        print(datetime.now())

    def closeEvent(self, event):
        print("ON CLOSE")
        self.vista_lista_veicoli.controller.save_data()
        event.accept()
