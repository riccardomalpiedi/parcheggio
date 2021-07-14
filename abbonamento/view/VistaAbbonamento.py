from PyQt5.QtWidgets import QDialog, QMessageBox
from datetime import datetime
from PyQt5.uic import loadUi

from abbonamento.controller.ControlloreAbbonamento import ControlloreAbbonamento
from abbonamento.model.Abbonamento import Abbonamento


class VistaAbbonamento(QDialog):
    def __init__(self, abbonamento, callback_inserisci_abbonamento):
        super(VistaAbbonamento, self).__init__()

        self.controller = ControlloreAbbonamento(abbonamento)
        self.callback_inserisci_abbonamento = callback_inserisci_abbonamento

        if self.controller.is_abbonato():
            loadUi("VistaAbbonamento1.ui", self)
            self.scadenza_label.setText("<font color='white'>" + self.controller.get_scadenza_string())
        else:
            loadUi("VistaAbbonamento2.ui", self)
            self.cliente_non_abbonato_label.setText("Cliente non abbonato")
            self.frase_label.setText("Aggiungi nuova data scadenza abbonamento (dd/MM/yyyy)")
            self.scadenza_lineedit.text()
            self.inserisci_button.clicked.connect(self.add_abbonamento_click)

    def add_abbonamento_click(self):
        try:
            print(self.scadenza_lineedit.text())
            date = datetime.strptime(self.scadenza_lineedit.text(), '%d/%m/%Y')
            print(date)
            print(date.timestamp())
            self.callback_inserisci_abbonamento(Abbonamento(date.timestamp()))
            self.close()
        except:
            QMessageBox.critical(self, 'Errore', "Inserisci la data nel formato richiesto: dd/MM/yyyy", QMessageBox.Ok,
                                 QMessageBox.Ok)
