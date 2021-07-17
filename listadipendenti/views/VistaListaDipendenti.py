from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from dipendente.views.VistaDipendente import VistaDipendente
from listadipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from listadipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente


class VistaListaDipendenti(QDialog):
    def __init__(self):
        super(VistaListaDipendenti, self).__init__()
        loadUi("listadipendenti.ui", self)

        self.controller = ControlloreListaDipendenti()

        self.list_view = QListView()
        self.update_ui()
        self.dipendenti_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)
        self.new_button.clicked.connect(self.show_new_dipendente)

        self.setWindowTitle("Lista Dipendenti")
        self.setFixedHeight(361)
        self.setFixedWidth(709)
        self.setWindowIcon(QIcon("icone/accountant2.png"))

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            self.vista_dipendente = VistaDipendente(dipendente_selezionato, self.controller.elimina_dipendente_by_id,
                                                    self.update_ui)
            self.vista_dipendente.show()

    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    def closeEvent(self, event):
        self.controller.save_data()