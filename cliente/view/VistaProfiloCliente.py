import os
import pickle

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from cliente.view.ModificaPasswordCliente import ModificaPasswordCliente
from listaveicoli.view.VistaListaVeicoliCliente import VistaListaVeicoliCliente
from cliente.view.ModificaProfiloCliente import ModificaProfiloCliente
from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaProfiloCliente(QDialog):
    def __init__(self, cliente, update_list, elimina_cliente):
        super(VistaProfiloCliente, self).__init__()
        loadUi("cliente/view/VistaProfiloCliente.ui", self)

        self.controller = ControlloreCliente(cliente)
        self.update_list = update_list
        self.update_ui()
        self.elimina_cliente = elimina_cliente

        self.gestione_veicoli_button.clicked.connect(self.go_gestione_veicoli_function)
        self.modifica_profilo_button.clicked.connect(self.go_modifica_profilo_function)
        self.modifica_password_button.clicked.connect(self.go_modifica_password)
        self.elimina_profilo_button.clicked.connect(self.go_elimina_profilo_function)

        self.setWindowTitle("Profilo Utente")
        self.setWindowIcon(QIcon("icone/user2.png"))
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def go_gestione_veicoli_function(self):
        self.gestione_veicoli_function = VistaListaVeicoliCliente(self.update_ui, self.controller.get_lista_dei_veicoli,
                                                                  self.controller.set_lista_dei_veicoli)
        self.gestione_veicoli_function.show()

    def go_modifica_profilo_function(self):
        self.modifica_profilo_function = ModificaProfiloCliente(self.controller, self.update_ui)
        self.modifica_profilo_function.show()

    def go_modifica_password(self):
        self.modifica_password = ModificaPasswordCliente(self.controller)
        self.modifica_password.show()

    def go_elimina_profilo_function(self):
        if self.controller.get_lista_dei_veicoli() is not None:
            for veicolo in self.controller.get_lista_dei_veicoli():
                if veicolo.orario_ingresso is not None:
                    QMessageBox.critical(self, "Attenzione", "Impossibile eliminare il profilo: uno dei suoi veicoli "
                                         "si trova ancora all'interno del parcheggio.",
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
                if veicolo.prenotazione is not None:
                    QMessageBox.critical(self, "Attenzione", "Impossibile eliminare il profilo: uno dei suoi veicoli "
                                         "ha una prenotazione attiva.",
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        reply = QMessageBox.question(self, "Attenzione", "Sei sicuro? Tutti i tuoi dati andranno persi.",
                                     QMessageBox.Ok, QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.elimina_cliente(self.controller.get_id_cliente())
            if self.controller.get_lista_dei_veicoli() is not None and self.controller.get_lista_dei_veicoli():
                lista_veicoli = []
                if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
                    with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                        lista_veicoli = pickle.load(f)
                for veicolo in self.controller.get_lista_dei_veicoli():
                    for veicolo2 in lista_veicoli:
                        if veicolo.id == veicolo2.id:
                            lista_veicoli.remove(veicolo2)
                with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
                    pickle.dump(lista_veicoli, handle, pickle.HIGHEST_PROTOCOL)
            self.close()

    def update_ui(self):
        self.nome_label.setText(
            "<font color='white'>" + self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        self.username_label.setText("<font color='white'>Username: " + self.controller.get_username_cliente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_cliente())
        self.indirizzo_label.setText("<font color='white'>Indirizzo: " + self.controller.get_indirizzo_cliente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_cliente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_cliente())

        self.veicolo_label.setText("")
        self.tipo_veicolo_label.setText("")
        self.veicolo2_label.setText("")
        self.tipo_veicolo2_label.setText("")
        if self.controller.get_lista_dei_veicoli() is None or len(self.controller.get_lista_dei_veicoli()) == 0:
            self.veicolo_label.setText("<font color='white'>Nessun veicolo associato")
        else:
            self.veicolo_label.setText("<font color='white'>Targa Veicolo: " +
                                       self.controller.get_veicolo_by_index(0).targa)
            self.tipo_veicolo_label.setText("<font color='white'>Tipo: " + self.controller.get_veicolo_by_index(0).tipo)
            if len(self.controller.get_lista_dei_veicoli()) > 1:
                self.veicolo2_label.setText("<font color='white'>Targa Veicolo2: " +
                                            self.controller.get_veicolo_by_index(1).targa)
                self.tipo_veicolo2_label.setText(
                    "<font color='white'>Tipo: " + self.controller.get_veicolo_by_index(1).tipo)

        self.photo_label.setPixmap(QPixmap(self.controller.get_image_cliente()))

    def closeEvent(self, event):
        self.update_list()
