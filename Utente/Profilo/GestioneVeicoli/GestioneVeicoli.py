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
        for veicolo in self.cliente.lista_veicoli:
            if veicolo is not None:
                item = QStandardItem()
                print(veicolo)
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
