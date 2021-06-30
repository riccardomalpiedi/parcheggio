from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QGridLayout, QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaposteggi.controller.ControlloreListaPosteggi import ControlloreListaPosteggi
from posteggio.views.VistaPosteggio import VistaPosteggio


class VistaListaPosteggi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPosteggi, self).__init__(parent)

        self.controller = ControlloreListaPosteggi()

        h_layout = QHBoxLayout()
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
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Posteggi')

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        posteggio_selezionato = self.controller.get_posteggio_by_index(selected)
        self.vista_posteggio = VistaPosteggio(posteggio_selezionato)
        self.vista_posteggio.show()