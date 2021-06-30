from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from veicolo.model.Veicolo import Veicolo


class VistaInserisciVeicolo(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciVeicolo, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()

        v_layout.addWidget(QLabel("Targa"))
        self.text_targa = QLineEdit(self)
        v_layout.addWidget(self.text_targa)

        v_layout.addWidget(QLabel("Tipo"))
        self.text_tipo = QLineEdit(self)
        v_layout.addWidget(self.text_tipo)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_veicolo)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Veicolo')

    def add_veicolo(self):
        targa = self.text_targa.text()
        tipo = self.text_tipo.text()

        if(targa == "" or tipo == ""):
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_veicolo(Veicolo(( 0  , targa, tipo)))
            self.callback()
            self.close()