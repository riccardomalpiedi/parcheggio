from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from posteggio.controller.ControllorePosteggio import ControllorePosteggio


class VistaPosteggio(QWidget):
    def __init__(self, posteggio, parent=None):
        super(VistaPosteggio, self).__init__(parent)
        self.controller = ControllorePosteggio(posteggio)
        loadUi("posteggio.ui", self)

        self.label_tipo.setText("<font color='white'>Tipo: " + self.controller.get_tipo_posteggio())
        self.label_titolo.setText("<font color='white'>" + self.controller.get_nome_posteggio())
        self.label_disponibile.setText("<font color='white'>" + self.controller.get_posteggio_disponibile())
        self.label_tariffa_oraria.setText(
            "<font color='white'>Tariffa oraria: €" + self.controller.get_tariffa_oraria_posteggio())
        self.label_tariffa_giornaliera_prenotazioni.setText("<font color='white'>Tariffa giornaliera prenotazioni: €"
                                + self.controller.get_tariffa_giornaliera_prenotazioni_posteggio())

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle(posteggio.nome)
        self.setWindowIcon(QIcon("icone/car2.png"))
