from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaListaPrenotazioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)
        grid_layout = QGridLayout()