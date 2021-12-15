from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QDialog, QListView
from PyQt5.uic import loadUi

from listaposteggi.controller.ControlloreListaPosteggi import ControlloreListaPosteggi
from posteggio.views.VistaPosteggio import VistaPosteggio


class VistaListaPosteggi(QDialog):
    def __init__(self):
        super(VistaListaPosteggi, self).__init__()
        loadUi("listaposteggi/views/VistaListaPosteggi.ui", self)

        self.controller = ControlloreListaPosteggi()

        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for posteggio in self.controller.get_lista_dei_posteggi():
            item = QStandardItem()
            item.setText(posteggio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        self.posteggi_layout.addWidget(self.list_view)

        self.open_button.clicked.connect(self.show_selected_info)

        self.setWindowTitle("Lista Posteggi")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/car2.png"))

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        if self.list_view.selectedIndexes() is None or not self.list_view.selectedIndexes():
            return
        selected = self.list_view.selectedIndexes()[0].row()
        posteggio_selezionato = self.controller.get_posteggio_by_index(selected)
        self.vista_posteggio = VistaPosteggio(posteggio_selezionato)
        self.vista_posteggio.show()
