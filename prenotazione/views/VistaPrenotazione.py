from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QGridLayout

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from prenotazione.model.Prenotazione import Prenotazione

class VistaPrenotazione(QWidget):
    def __init__(self, parent=None):
        super(VistaPrenotazione, self).__init__(parent)

        self.controller = ControllorePrenotazione(Prenotazione)
        self.disdisci_prenotazione = self.disdisci_prenotazione
        self.elimina_callback = self.elimina_callback

        grid_layout = QGridLayout()

        label_nome = QLabel(self.controller.get_servizio_prenotazione().nome)
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

        label_datanascita = QLabel("Data: {}".format(self.controller.get_data_prenotazione()))
        font_datanascita = label_datanascita.font()
        font_datanascita.setPointSize(17)
        label_datanascita.setFont(font_datanascita)
        grid_layout.addWidget(label_datanascita)

        grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        grid_layout.addWidget(btn_disdici)

        self.setLayout(grid_layout)

    def disdici_prenotazione_click(self):
        self.disdisci_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()