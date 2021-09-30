from datetime import datetime

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        loadUi("Ingresso.ui", self)
        self.controller = ControlloreListaVeicoli()
        self.update_ui()

        self.pushButton.clicked.connect(self.go_vista_inserisci_veicolo)
        self.entra_button.clicked.connect(self.inserisci_ingresso_veicolo)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

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
        if veicolo.orario_ingresso is not None:
            QMessageBox.critical(self, 'Errore', "Il veicolo si trova già nel parcheggio",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            veicolo.set_orario_ingresso(datetime.now())
            self.controller.save_data()
            QMessageBox.information(self, "Operazione riuscita", "Benvenuto nel nostro parcheggio")
            self.close()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
