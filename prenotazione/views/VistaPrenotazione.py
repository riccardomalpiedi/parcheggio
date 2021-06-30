from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaPrenotazione(QWidget):
    def __init__(self, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        grid_layout = QGridLayout()