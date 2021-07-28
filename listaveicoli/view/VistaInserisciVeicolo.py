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

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Veicolo')

    def add_veicolo(self):
        targa = self.targa_lineEdit.text()
        tipo = self.tipo_veicolo_lineEdit.text()

        if targa == "" or tipo == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_veicolo(Veicolo(targa.lower(), targa, tipo))
            self.callback()
            self.close()
