from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaUtente(QWidget):
    def __init__(self, parent=None):
        super(VistaUtente, self).__init__(parent)
        grid_layout = QGridLayout()