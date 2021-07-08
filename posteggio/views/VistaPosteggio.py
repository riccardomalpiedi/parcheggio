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
        self.label_prezzo.setText("<font color='white'>Prezzo: €" + self.controller.get_prezzo_posteggio())

        self.setWindowTitle(posteggio.nome)
