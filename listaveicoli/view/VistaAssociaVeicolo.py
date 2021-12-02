from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from listaveicoli.view.VistaInserisciVeicolo import VistaInserisciVeicolo


class VistaAssociaVeicolo(QDialog):
    def __init__(self, controller, callback, get_lista_veicoli, set_lista_veicoli):
        super(VistaAssociaVeicolo, self).__init__()
        loadUi("listaveicoli/view/VistaAssociaVeicolo.ui", self)

        self.controller = controller
        self.callback = callback
        self.get_lista_veicoli = get_lista_veicoli
        self.set_lista_veicoli = set_lista_veicoli

        self.inserisci_button.clicked.connect(self.add_veicolo)
        self.registra_button.clicked.connect(self.show_new_veicolo)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Associa Veicolo')

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
                        self.controller.get_veicolo_by_id(veicolo.id).associato = True
                        if self.get_lista_veicoli() is not None:
                            self.get_lista_veicoli().append(veicolo)
                        else:
                            lista_veicoli = [veicolo]
                            self.set_lista_veicoli(lista_veicoli)

            if not trovato:
                QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non è registrato",
                                     QMessageBox.Ok, QMessageBox.Ok)
            self.callback()
            self.close()
