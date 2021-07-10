from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo
from listaveicoli.view.VistaListaVeicoli import VistaListaVeicoli


class VistaIngresso(QWidget):
    def __init__(self):
        super(VistaIngresso, self).__init__()
        self.vista_lista_veicoli = VistaListaVeicoli()
        self.controller = self.vista_lista_veicoli.controller
        loadUi("Ui_Ingresso.ui", self)
        self.inserisci_veicolo_button.clicked.connect(self.go_vista_inserisci_veicolo)

    def go_vista_inserisci_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.vista_lista_veicoli.update_ui)
        self.vista_inserisci_veicolo.show()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
