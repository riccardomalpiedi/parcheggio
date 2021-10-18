from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VistaInserisciPrenotazione(QDialog):
    def __init__(self, controller):
        super(VistaInserisciPrenotazione, self).__init__()
        loadUi("NuovaPrenotazione.ui", self)

        self.controller = controller
