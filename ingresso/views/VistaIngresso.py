from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from ingresso.views.Ui_Ingresso import Ui_Ingresso


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        self.ui = Ui_Ingresso()
        self.ui.setupUi(self)
