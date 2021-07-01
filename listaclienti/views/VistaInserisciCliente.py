from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Cognome"))
        self.text_cognome = QLineEdit(self)
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("Codice Fiscale"))
        self.text_cf = QLineEdit(self)
        v_layout.addWidget(self.text_cf)

        v_layout.addWidget(QLabel("Indirizzo"))
        self.text_indirizzo = QLineEdit(self)
        v_layout.addWidget(self.text_indirizzo)

        v_layout.addWidget(QLabel("Email"))
        self.text_email = QLineEdit(self)
        v_layout.addWidget(self.text_email)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_cliente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Cliente')

    def add_cliente(self):
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        cf = self.text_cf.text()
        indirizzo = self.text_indirizzo.text()
        email = self.text_email.text()
        telefono = self.text_telefono.text()

        if(nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" ):
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_cliente(Cliente((nome+cognome).lower(), nome, cognome, cf, indirizzo, email, telefono))
            self.callback()
            self.close()