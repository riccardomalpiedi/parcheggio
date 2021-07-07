from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo
from veicolo.view.VistaVeicolo import VistaVeicolo


class VistaListaVeicoli(QWidget):
    def __init__(self, parent=None):
        super(VistaListaVeicoli, self).__init__(parent)

        self.controller = ControlloreListaVeicoli()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        for veicolo in self.controller.get_lista_dei_veicoli():
            item = QStandardItem()
            item.setText(veicolo.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_veicolo)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Veicoli')

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.controller.get_veicolo_by_index(selected)
        self.vista_veicolo = VistaVeicolo(veicolo_selezionato, self.controller.elimina_veicolo_by_id, self.update_ui)
        self.vista_veicolo.show()

    def show_new_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.update_ui)
        self.vista_inserisci_veicolo.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for veicolo in self.controller.get_lista_dei_veicoli():
            item = QStandardItem()
            item.setText("Targa: "+veicolo.traga)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
