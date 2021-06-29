from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        Cassiere_button = QPushButton("Vista Cassiere")
        Cassiere_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Cassiere_button.clicked.connect(self.go_VistaCassiere)

        Clienti_button = QPushButton('Vista Clienti')
        Clienti_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Clienti_button.clicked.connect(self.go_VistaClienti)

        Amministratore_button = QPushButton('Lista Dipendenti')
        Amministratore_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Amministratore_button.clicked.connect(self.go_VistaAmministratore)

        grid_layout.addWidget(Cassiere_button, 0, 0)
        grid_layout.addWidget(Clienti_button, 0, 1)
        grid_layout.addWidget(Amministratore_button, 1, 0)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle('Gestore Parcheggio')

    def go_VistaCassiere(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_VistaClienti(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_VistaAmministratore(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()