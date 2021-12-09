from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QDialog, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.view.VistaAssociaVeicolo import VistaAssociaVeicolo
from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from veicolo.view.VistaVeicoloCliente import VistaVeicoloCliente


class VistaListaVeicoliCliente(QDialog):
    def __init__(self, callback, get_lista_veicoli, set_lista_veicoli):
        super(VistaListaVeicoliCliente, self).__init__()
        loadUi("listaveicoli/view/VistaListaVeicoliCliente.ui", self)

        self.controller = ControlloreListaVeicoli()
        self.callback = callback
        # Questi metodi servono alla classe per visualizzare e aggiornare la lista dei veicoli associati al cliente
        self.get_lista_veicoli = get_lista_veicoli
        self.set_lista_veicoli = set_lista_veicoli

        self.list_view = QListView()
        self.update_ui()
        self.veicoli_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)
        self.new_button.clicked.connect(self.show_new_veicolo)

        self.setWindowTitle("Lista Veicoli")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

    def show_selected_info(self):
        if self.list_view.selectedIndexes() is None or not self.list_view.selectedIndexes():
            return
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.get_lista_veicoli()[selected]
        self.vista_veicolo = VistaVeicoloCliente(veicolo_selezionato, self.elimina_veicolo, self.update_prenotazione,
                                                 self.update_ui)
        self.vista_veicolo.show()

    def show_new_veicolo(self):
        if self.get_lista_veicoli() is not None and len(self.get_lista_veicoli()) > 1:
            QMessageBox.critical(self, 'Errore', "Limite massimo di veicoli raggiunto",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_inserisci_veicolo = VistaAssociaVeicolo(self.controller, self.update_ui, self.get_lista_veicoli,
                                                           self.set_lista_veicoli)
        self.vista_inserisci_veicolo.show()

    def elimina_veicolo(self, id):
        self.controller.elimina_veicolo_by_id(id)
        lista_veicoli = self.get_lista_veicoli()
        for veicolo in lista_veicoli:
            if veicolo.id == id:
                lista_veicoli.remove(veicolo)
        self.set_lista_veicoli(lista_veicoli)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        if self.get_lista_veicoli() is not None:
            for veicolo in self.get_lista_veicoli():
                item = QStandardItem()
                item.setText(veicolo.targa)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        self.callback()

    def update_prenotazione(self, id, prenotazione):
        if self.controller.get_veicolo_by_id(id) is None:
            return
        self.controller.get_veicolo_by_id(id).prenotazione = prenotazione

    def closeEvent(self, event):
        self.controller.save_data()
