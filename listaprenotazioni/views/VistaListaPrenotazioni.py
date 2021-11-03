from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioni(QDialog):
    def __init__(self):
        super(VistaListaPrenotazioni, self).__init__()
        loadUi("listaprenotazioni/views/ListaPrenotazioniAmministratore.ui", self)

        self.controller = ControlloreListaPrenotazioni()

        self.list_view = QListView()
        self.update_ui()
        self.prenotazioni_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)

        self.setWindowTitle("Lista Prenotazioni")
        self.setFixedHeight(361)
        self.setFixedWidth(709)
        self.setWindowIcon(QIcon("icone/booking2.png"))

    def show_selected_info(self):
        if self.list_view.selectedIndexes() is None or not self.list_view.selectedIndexes():
            return
        selected = self.list_view.selectedIndexes()[0].row()
        prenotazione_selezionato = self.controller.get_prenotazione_by_index(selected)
        self.vista_prenotazione = VistaPrenotazione(prenotazione_selezionato,
                                                    self.controller.elimina_prenotazione_by_id, self.update_ui)
        self.vista_prenotazione.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.controller.get_lista_delle_prenotazioni():
            item = QStandardItem()
            item.setText(prenotazione.cliente.cognome + ": " + prenotazione.cliente.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
