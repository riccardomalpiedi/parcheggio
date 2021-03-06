from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from cliente.view.VistaCliente import VistaCliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti

# Vista contenente la lista di tutti i cliente, accedibile solo all'amministratore
class VistaListaClienti(QDialog):
    def __init__(self):
        super(VistaListaClienti, self).__init__()
        loadUi("listaclienti/views/VistaListaClienti.ui", self)

        self.controller = ControlloreListaClienti()
        self.list_view = QListView()
        self.update_ui()

        self.clienti_layout.addWidget(self.list_view)
        self.open_button.clicked.connect(self.show_selected_info)

        self.setWindowTitle("Lista Clienti")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/user2.png"))

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if self.list_view.selectedIndexes() is None or not self.list_view.selectedIndexes():
            return
        selected = self.list_view.selectedIndexes()[0].row()
        cliente_selezionato = self.controller.get_cliente_by_index(selected)
        self.vista_cliente = VistaCliente(cliente_selezionato)
        self.vista_cliente.show()

    def closeEvent(self, event):
        self.controller.save_data()
