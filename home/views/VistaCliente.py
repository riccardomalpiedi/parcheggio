from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaCliente(QWidget):
    def __init__(self, parent=None):
        super(VistaCliente, self).__init__(parent)
        grid_layout = QGridLayout()