from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo


class GestioneInserisciVeicoli(QDialog):
    def __init__(self, controller, callback, update_lista_veicoli, lista_veicoli):
        super(GestioneInserisciVeicoli, self).__init__()
        loadUi("Utente/Profilo/GestioneVeicoli/GestioneNuovoVeicolo.ui", self)

        self.controller = controller
        self.callback = callback
        self.update_lista_veicoli = update_lista_veicoli
        self.lista_veicoli = lista_veicoli

        self.inserisci_button.clicked.connect(self.add_veicolo)
        self.registra_button.clicked.connect(self.show_new_veicolo)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Veicolo')

    def show_new_veicolo(self):
        self.vista_inserisci_veicolo = VistaInserisciVeicolo(self.controller, self.callback)
        self.vista_inserisci_veicolo.show()

    def add_veicolo(self):
        targa = self.targa_lineEdit.text()

        if targa == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            trovato = False
            for veicolo in self.controller.get_lista_dei_veicoli():
                if targa == veicolo.targa:
                    trovato = True
                    if veicolo.get_associato():
                        QMessageBox.critical(self, 'Errore', "Il veicolo selezionato è già associato a un cliente",
                                             QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        self.lista_veicoli.append(veicolo)
                        self.update_lista_veicoli()
            if not trovato:
                QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non è registrato",
                                     QMessageBox.Ok, QMessageBox.Ok)
            self.callback()
            self.close()

    def closeEvent(self, event):
        self.controller.save_data()
