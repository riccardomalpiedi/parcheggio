from PyQt5.QtWidgets import QWidget, QGridLayout


class VistaCassiere(QWidget):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        grid_layout = QGridLayout()