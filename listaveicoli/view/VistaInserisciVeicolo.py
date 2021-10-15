from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from veicolo.model.Veicolo import Veicolo


class VistaInserisciVeicolo(QDialog):
    def __init__(self, controller, callback):
        super(VistaInserisciVeicolo, self).__init__()
        loadUi("NuovoVeicolo.ui", self)

        self.controller = controller
        self.callback = callback

        self.ok_button.clicked.connect(self.add_veicolo)

        self.combotipo_model = QStandardItemModel(self.tipo_comboBox)
        item = QStandardItem()
        item.setText("Auto")
        item.setEditable(False)
        font = item.font()
        font.setPointSize(18)
        item.setFont(font)
        self.combotipo_model.appendRow(item)

        item1 = QStandardItem()
        item1.setText("Moto")
        item1.setEditable(False)
        font1 = item1.font()
        font1.setPointSize(18)
        item1.setFont(font1)
        self.combotipo_model.appendRow(item1)

        item2 = QStandardItem()
        item2.setText("Camion")
        item2.setEditable(False)
        font2 = item2.font()
        font2.setPointSize(18)
        item2.setFont(font2)
        self.combotipo_model.appendRow(item2)
        self.tipo_comboBox.setModel(self.combotipo_model)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Veicolo')

    def add_veicolo(self):
        targa = self.targa_lineEdit.text()
        tipo = self.tipo_comboBox.currentText()

        if targa == "" or tipo == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_veicolo(Veicolo(targa.lower(), targa, tipo))
            if self.callback is not None:
                self.callback()
            self.close()
