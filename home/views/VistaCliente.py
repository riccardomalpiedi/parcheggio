from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from ingresso.views.Ui_Ingresso import Ui_Ingresso


class VistaCliente(QWidget):
    def __init__(self, parent=None):
        super(VistaCliente, self).__init__(parent)
        grid_layout = QGridLayout()

        vista_ingresso_button = self.create_button("Vista Ingresso", "icone/cash2.png", self.go_vista_ingresso)
        vista_uscita_button = self.create_button("Vista Uscita", "icone/user2.png", self.go_vista_uscita)

        grid_layout.addWidget(vista_ingresso_button, 0, 0)
        grid_layout.addWidget(vista_uscita_button, 0, 1)
        self.setLayout(grid_layout)
        self.resize(500, 400)
        self.setWindowTitle('Vista Cliente')

    def create_button(self, titolo, icona, on_click=None):
        button = QPushButton(titolo)
        button.setFont(QFont("arial", 12))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        # button.setIcon(QIcon(icona))
        return button

    def go_vista_ingresso(self):
        Ingresso = QWidget()
        ui = Ui_Ingresso()
        ui.setupUi(Ingresso)
        Ingresso.show()

    def go_vista_uscita(self):
        # self.vista_uscita = VistaUscita()
        # self.vista_uscita.show()
        pass