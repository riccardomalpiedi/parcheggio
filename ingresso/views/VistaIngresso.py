from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        loadUi("Ui_Ingresso.ui", self)
