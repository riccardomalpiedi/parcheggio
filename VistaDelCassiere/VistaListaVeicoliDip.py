from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
# from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo
# from veicolo.view.VistaVeicolo import VistaVeicolo
from veicolo.view.VistaVeicoloDipendente import VistaVeicoloDipendente


class VistaListaVeicoliDip(QDialog):
    def __init__(self):
        super(VistaListaVeicoliDip, self).__init__()
        loadUi("VistaDelCassiere/ListaVeicoliDip.ui", self)

        self.controller = ControlloreListaVeicoli()

        self.list_view = QListView()
        self.update_ui()
        self.veicoli_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)
        # self.new_button.clicked.connect(self.show_new_veicolo)
        self.back_button.clicked.connect(self.go_back)

        self.setWindowTitle("Lista Veicoli")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.controller.get_veicolo_by_index(selected)
        self.vista_veicolo = VistaVeicoloDipendente(veicolo_selezionato, self.controller.elimina_veicolo_by_id, self.update_ui)
        self.vista_veicolo.show()

    def show_new_veicolo(self):
        # self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.update_ui)
        # self.vista_inserisci_veicolo.show()
        pass

    def go_back(self):
        self.close()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for veicolo in self.controller.get_lista_dei_veicoli():
            item = QStandardItem()
            item.setText("Targa: " + veicolo.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()