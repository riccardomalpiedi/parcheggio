from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from veicolo.view.VistaVeicoloAmministratore import VistaVeicoloAmministratore


class VistaListaVeicoliAmministratore(QDialog):
    def __init__(self):
        super(VistaListaVeicoliAmministratore, self).__init__()
        loadUi("listaveicoli/view/VistaListaVeicoliAmministratore.ui", self)

        self.controller = ControlloreListaVeicoli()

        self.list_view = QListView()
        self.update_ui()
        self.veicoli_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)

        self.setWindowTitle("Lista Veicoli")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

    def show_selected_info(self):
        if self.list_view.selectedIndexes() is None or not self.list_view.selectedIndexes():
            return
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.controller.get_veicolo_by_index(selected)
        self.vista_veicolo = VistaVeicoloAmministratore(veicolo_selezionato)
        self.vista_veicolo.show()

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
