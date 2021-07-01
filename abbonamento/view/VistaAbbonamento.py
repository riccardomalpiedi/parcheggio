from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton

from abbonamento.controller.ControlloreAbbonamento import ControlloreAbbonamento
from abbonamento.model.Abbonamento import Abbonamento


class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, callback_inserisci_abbonamento):
        super(VistaAbbonamento, self).__init__()
        self.controller = ControlloreAbbonamento(abbonamento)
        self.callback_inserisci_abbonamento = callback_inserisci_abbonamento

        v_layout = QVBoxLayout()
        if(self.controller.is_abbonato()):
            v_layout.addWidget(QLabel(self.controller.get_scadenza_string()))
        else:
            v_layout.addWidget(QLabel("Cliente non abbonato"))
            v_layout.addWidget(QLabel("Aggiungi nuova data scadenza abbonamento (dd/MM/yyyy"))
            self.text_scadenza = QLineEdit()
            v_layout.addWidget(self.text_scadenza)
            btn_inserisci = QPushButton("Aggiungi")
            btn_inserisci.clicked.connect(self.add_abbonamento_click)
            v_layout.addWidget(btn_inserisci)

        self.setLayout(v_layout)

    def add_abbonamento_click(self):
        try:
            print(self.text_scadenza.text())
            date = datetime.strptime(self.text_scadenza.text(), '%d/%m/%Y')
            print(date)
            print(date.timestamp())
            self.callback_inserisci_abbonamento(Abbonamento(date.timestamp()))
            self.close()
        except:
            QMessageBox.critical(self, 'Errore', "Inserisci la data nel formato richiesto: dd/MM/yyyy", QMessageBox.Ok, QMessageBox.Ok)
