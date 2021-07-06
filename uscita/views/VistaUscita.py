from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class VistaUscita(QWidget):
    def __init__(self):
        super(VistaUscita, self).__init__()
        loadUi("Ui_Uscita.ui", self)