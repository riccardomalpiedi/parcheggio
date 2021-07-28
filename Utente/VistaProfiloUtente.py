from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utente.Profilo.CambiaPassword.CambiaPassword import CambiaPassword
from Utente.Profilo.GestionePrenotazioni.GestionePrenotazioni import GestionePrenotazioni
from Utente.Profilo.GestioneVeicoli.GestioneVeicoli import GestioneVeicoli
from Utente.Profilo.ModificaProfilo.ModificaProfilo import ModificaProfilo
from cliente.controller.ControlloreCliente import ControlloreCliente


# from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaProfiloUtente(QDialog):
    def __init__(self, cliente):
        super(VistaProfiloUtente, self).__init__()
        loadUi("Utente/VistaProfiloUtente.ui", self)
        self.cliente = cliente
        self.controller = ControlloreCliente(self.cliente)

        # self.controller1 = ControlloreListaClienti()
        # self.list_view = QListView()
        # self.update_ui()

        self.nome_label.setText(
            "<font color='white'>" + self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        self.username_label.setText("<font color='white'>Username: " + self.controller.get_username_cliente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_cliente())
        self.indirizzo_label.setText("<font color='white'>Indirizzo: " + self.controller.get_indirizzo_cliente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_cliente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_cliente())
        if self.controller.get_veicolo_cliente() is not None:
            self.veicolo_label.setText("<font color='white'>Targa Veicolo: " +
                                       self.controller.get_veicolo_cliente().targa)
            self.tipo_veicolo_label.setText("<font color='white'>Tipo: " + self.controller.get_veicolo_cliente().tipo)
        if self.controller.get_veicolo2_cliente() is not None:
            self.veicolo2_label.setText(self.veicolo_label.text() + " <font color='white'>Targa Veicolo2: " +
                                        self.controller.get_veicolo2_cliente().targa)
            self.tipo_veicolo2_label.setText("<font color='white'>Tipo: " + self.controller.get_veicolo2_cliente().tipo)
        if self.controller.get_veicolo_cliente() is None and self.controller.get_veicolo2_cliente() is None:
            self.veicolo_label.setText("<font color='white'>Nessun veicolo associato")

        self.photo_label.setPixmap(QPixmap(self.controller.get_image_cliente()))

        self.gestione_veicoli_button.clicked.connect(self.go_gestione_veicoli_function)
        self.gestione_prenotazioni_button.clicked.connect(self.go_gestisci_prenotazioni_function)
        self.modifica_profilo_button.clicked.connect(self.go_modifica_profilo_function)
        self.cambia_password_button.clicked.connect(self.go_modifica_password)

        self.setWindowTitle("Profilo Utente")
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())

    def go_gestione_veicoli_function(self):
        self.gestione_veicoli_function = GestioneVeicoli(self.cliente)
        self.gestione_veicoli_function.show()

    def go_gestisci_prenotazioni_function(self):
        self.gestisci_prenotazioni_function = GestionePrenotazioni(self.cliente)
        self.gestisci_prenotazioni_function.show()

    def go_modifica_profilo_function(self):
        self.modifica_profilo_function = ModificaProfilo()
        # self.modifica_profilo_function = ModificaProfilo(self.cliente, self.controller1, self.update_ui)
        self.modifica_profilo_function.show()

    def go_modifica_password(self):
        self.modifica_password = CambiaPassword()
        self.modifica_password.show()

    # def update_ui(self):
    #     self.listview_model = QStandardItemModel(self.list_view)
    #     for cliente in self.controller1.get_lista_dei_clienti():
    #         item = QStandardItem()
    #         item.setText(cliente.nome + " " + cliente.cognome)
    #         item.setEditable(False)
    #         font = item.font()
    #         font.setPointSize(18)
    #         item.setFont(font)
    #         self.listview_model.appendRow(item)
    #     self.list_view.setModel(self.listview_model)
