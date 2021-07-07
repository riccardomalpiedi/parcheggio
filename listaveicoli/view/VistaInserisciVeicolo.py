from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from veicolo.model.Veicolo import Veicolo


class VistaInserisciVeicolo(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciVeicolo, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()

        self.qlines = {}
        self.add_info_text("targa", "Targa")
        self.add_info_text("tipo", "TIpo")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_veicolo)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle('Nuovo Veicolo')

    def add_veicolo(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return

        self.controller.aggiungi_veicolo(Veicolo(
            (self.qlines["targa"].text() ).lower(),
            self.qlines["tipo"].text(),)
        )

        self.callback()
        self.close()
