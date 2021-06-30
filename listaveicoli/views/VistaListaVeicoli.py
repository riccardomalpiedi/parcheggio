from PyQt5.QtWidgets import QGridLayout, QWidget


class VistaListaVeicoli(QWidget):
    def __init__(self, parent=None):
        super(VistaListaVeicoli, self).__init__(parent)
        grid_layout = QGridLayout()