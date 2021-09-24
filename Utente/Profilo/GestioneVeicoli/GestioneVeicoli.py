from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QDialog, QMessageBox
from PyQt5.uic import loadUi

from Utente.Profilo.GestioneVeicoli.GestioneInserisciVeicolo import GestioneInserisciVeicoli
from listaveicoli.controller.ControlloreListaVeicoli import ControlloreListaVeicoli
from veicolo.view.VistaVeicolo import VistaVeicolo


class GestioneVeicoli(QDialog):
    def __init__(self, cliente, callback, controller):
        super(GestioneVeicoli, self).__init__()
        loadUi("Utente/Profilo/GestioneVeicoli/GestioneVeicoli.ui", self)

        self.controller = ControlloreListaVeicoli()
        self.controller2 = controller
        self.cliente = cliente
        self.callback = callback

        self.list_view = QListView()
        self.update_ui()
        self.veicoli_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)
        self.new_button.clicked.connect(self.show_new_veicolo)

        self.setWindowTitle("Lista Veicoli")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        veicolo_selezionato = self.cliente.lista_veicoli[selected]
        self.vista_veicolo = VistaVeicolo(veicolo_selezionato, self.elimina_veicolo, self.update_ui)
        self.vista_veicolo.show()

    def show_new_veicolo(self):
        if len(self.cliente.lista_veicoli) > 1:
            QMessageBox.critical(self, 'Errore', "Limite massimo di veicoli raggiunto",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_inserisci_veicolo = GestioneInserisciVeicoli(self.controller, self.controller2,
                                                                self.update_ui, self.cliente)
        self.vista_inserisci_veicolo.show()

    def elimina_veicolo(self, id):
        self.controller2.get_cliente_by_id(self.cliente.id).rimuovi_veicolo_by_id(id)
        self.controller.elimina_veicolo_by_id(id)
        self.controller2.save_data()

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
        self.callback()

    def closeEvent(self, event):
        self.controller.save_data()
        self.controller2.save_data()
