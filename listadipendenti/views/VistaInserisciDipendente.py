from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox


class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("luogo_n", "Luogo di nascita")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("licenza", "Licenza")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_dipendente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_dipendente(Dipendente(
            (self.qlines["nome"].text()+self.qlines["cognome"].text()).lower(),
            self.qlines["nome"].text(),
            self.qlines["cognome"].text(),
            self.qlines["data_n"].text(),
            self.qlines["luogo_n"].text(),
            self.qlines["cf"].text(),
            self.qlines["telefono"].text(),
            self.qlines["email"].text(),
            self.qlines["licenza"].text())
        )
        self.callback()
        self.close()