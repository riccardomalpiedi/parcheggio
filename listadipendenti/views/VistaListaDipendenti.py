from PyQt5.QtWidgets import QGridLayout, QWidget


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        grid_layout = QGridLayout()