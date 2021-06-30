from PyQt5.QtWidgets import QGridLayout, QWidget


class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        grid_layout = QGridLayout()