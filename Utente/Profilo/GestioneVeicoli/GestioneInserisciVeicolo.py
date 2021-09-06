from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class GestioneInserisciVeicoli(QDialog):
    def __init__(self, controller, callback, cliente):
        super(GestioneInserisciVeicoli, self).__init__()
        loadUi("Utente/Profilo/GestioneVeicoli/GestioneNuovoVeicolo.ui", self)

        self.controller = controller
        self.controller2 = ControlloreListaClienti()
        self.callback = callback
        self.cliente = cliente

        self.inserisci_button.clicked.connect(self.add_veicolo)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle('Nuovo Veicolo')

    def add_veicolo(self):
        targa = self.targa_lineEdit.text()

        if targa == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            flag = False
            for veicolo in self.controller.get_lista_dei_veicoli():
                if targa == veicolo.targa:
                    flag = True
                    if self.controller.get_veicolo_by_targa(targa).get_associato():
                        QMessageBox.critical(self, 'Errore', "Il veicolo selezionato è già associato a un cliente",
                                             QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        self.controller2.get_cliente_by_id(self.cliente.id).aggiungi_veicolo(veicolo)
                        self.controller.get_veicolo_by_targa(targa).set_associato(True)
            if not flag:
                QMessageBox.critical(self, 'Errore', "Il veicolo selezionato non è registrato",
                                     QMessageBox.Ok, QMessageBox.Ok)
            self.controller2.save_data()
            self.callback()
            self.close()
