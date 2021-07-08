from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QLabel, QLineEdit

from veicolo.model.Veicolo import Veicolo


class VistaInserisciVeicolo(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciVeicolo, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()

        self.qlines = {}
        self.add_info_text("targa", "Targa")
        self.add_info_text("tipo", "Tipo")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_veicolo)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle('Nuovo Veicolo')

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_veicolo(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return

        # id da cambiare
        self.controller.aggiungi_veicolo(Veicolo(
            "prova", (self.qlines["targa"].text()).lower(),
            self.qlines["tipo"].text())
        )

        self.callback()
        self.close()
