from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaAmministratore(QWidget):
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        grid_layout = QGridLayout()