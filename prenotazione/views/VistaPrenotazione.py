from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSpacerItem, QSizePolicy, QGridLayout

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione

class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)

        self.controller = ControllorePrenotazione(prenotazione)
        self.disdisci_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        grid_layout = QGridLayout()

        label_nome = QLabel(self.controller.get_posteggio_prenotazione().nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        grid_layout.addWidget(label_nome)

        grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf = QLabel("Cliente: {}".format(
            self.controller.get_cliente_prenotazione().nome + " " + self.controller.get_cliente_prenotazione().cognome))
        font_cf = label_cf.font()
        font_cf.setPointSize(17)
        label_cf.setFont(font_cf)
        grid_layout.addWidget(label_cf)

        label_data_inizio = QLabel("Data: {}".format(self.controller.get_data_inizio_prenotazione()))
        font_data_inizio = label_data_inizio.font()
        font_data_inizio.setPointSize(17)
        label_data_inizio.setFont(font_data_inizio)
        grid_layout.addWidget(label_data_inizio)

        label_data_fine = QLabel("Data: {}".format(self.controller.get_data_fine_prenotazione()))
        font_data_fine = label_data_fine.font()
        font_data_fine.setPointSize(17)
        label_data_fine.setFont(font_data_fine)
        grid_layout.addWidget(label_data_fine)

        grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        grid_layout.addWidget(btn_disdici)

        self.setLayout(grid_layout)

    def disdici_prenotazione_click(self):
        self.disdisci_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()