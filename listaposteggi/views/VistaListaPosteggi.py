from PyQt5.QtWidgets import QGridLayout, QWidget


class VistaListaPosteggi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPosteggi, self).__init__(parent)
        grid_layout = QGridLayout()