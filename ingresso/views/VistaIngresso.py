from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        self.controller = ControlloreListaVeicoli()
        loadUi("Ui_Ingresso.ui", self)
        self.inserisci_veicolo_button.clicked.connect(self.go_vista_inserisci_veicolo)

    def go_vista_inserisci_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.update_ui)
        self.vista_inserisci_veicolo.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for veicolo in self.controller.get_lista_dei_veicoli():
            item = QStandardItem()
            item.setText("Targa: "+veicolo.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
