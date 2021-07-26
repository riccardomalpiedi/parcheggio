from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QDialog
from PyQt5.uic import loadUi

from Utente.Profilo.GestioneVeicoli.GestioneInserisciVeicolo import GestioneInserisciVeicoli
from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from veicolo.view.VistaVeicolo import VistaVeicolo


class GestioneVeicoli(QDialog):
    def __init__(self, cliente):
        super(GestioneVeicoli, self).__init__()
        loadUi("Utente/Profilo/GestioneVeicoli/GestioneVeicoli.ui", self)

        self.controller = ControlloreListaVeicoli()
        self.cliente = cliente

        self.list_view = QListView()
        self.update_ui()
        self.veicoli_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)
        self.new_button.clicked.connect(self.show_new_veicolo)

        self.setWindowTitle("Lista Veicoli")
        self.setFixedHeight(361)
        self.setFixedWidth(709)

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.controller.get_veicolo_by_index(selected)
        self.vista_veicolo = VistaVeicolo(veicolo_selezionato, self.controller.elimina_veicolo_by_id, self.update_ui)
        self.vista_veicolo.show()

    def show_new_veicolo(self):
        self.vista_inserisci_veicolo = GestioneInserisciVeicoli(self.controller, self.update_ui)
        self.vista_inserisci_veicolo.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        item = QStandardItem()
        item2 = QStandardItem()
        print(self.cliente.veicolo)
        print(self.cliente.veicolo2)
        item.setText(self.cliente.veicolo.targa)
        item2.setText(self.cliente.veicolo2.targa)
        item.setEditable(False)
        item2.setEditable(False)
        font = item.font()
        font.setPointSize(18)
        font2 = item.font()
        font2.setPointSize(18)
        item.setFont(font)
        item2.setFont(font2)
        self.listview_model.appendRow(item)
        self.listview_model.appendRow(item2)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
