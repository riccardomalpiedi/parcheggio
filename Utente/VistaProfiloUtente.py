from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utente.Profilo.CambiaPassword.CambiaPassword import CambiaPassword
from Utente.Profilo.GestionePrenotazioni.GestionePrenotazione import GestionePrenotazioni
from Utente.Profilo.GestioneVeicoli.GestioneVeicoli import GestioneVeicoli
from Utente.Profilo.ModificaProfilo.ModificaProfilo import ModificaProfilo
from Utente.Profilo.UpdateFoto.UpdateFoto import UpdateFoto
from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaProfiloUtente(QDialog):
    def __init__(self, cliente):
        super(VistaProfiloUtente, self).__init__()
        loadUi("Utente/VistaProfiloUtente.ui", self)
        self.controller = ControlloreCliente(cliente)

        self.nome_label.setText(
            "<font color='white'>" + self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        self.username_label.setText("<font color='white'>Username: " + self.controller.get_username_cliente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_cliente())
        self.indirizzo_label.setText("<font color='white'>Indirizzo: " + self.controller.get_indirizzo_cliente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_cliente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_cliente())
        self.veicolo_label.setText("<font color='white'>Targa Veicolo: " + self.controller.get_veicolo_cliente())

        self.update_button.clicked.connect(self.go_update_function)
        self.gestione_veicoli_button.clicked.connect(self.go_gestione_veicoli_function)
        self.gestione_prenotazioni_button.clicked.connect(self.go_gestisci_prenotazioni_function)
        self.modifica_profilo_button.clicked.connect(self.go_modifica_profilo_function)
        self.cambia_password_button.clicked.connect(self.go_modifica_password)

        self.setWindowTitle("Profilo Utente")
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def go_update_function(self):
        self.update_function = UpdateFoto()
        self.update_function.show()

    def go_gestione_veicoli_function(self):
        self.gestione_veicoli_function = GestioneVeicoli()
        self.gestione_veicoli_function.show()

    def go_gestisci_prenotazioni_function(self):
        self.gestisci_prenotazioni_function = GestionePrenotazioni()
        self.gestisci_prenotazioni_function.show()

    def go_modifica_profilo_function(self):
        self.modifica_profilo_function = ModificaProfilo()
        self.modifica_profilo_function.show()

    def go_modifica_password(self):
        self.modifica_password = CambiaPassword()
        self.modifica_password.show()
