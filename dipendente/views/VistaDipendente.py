from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QDialog):
    def __init__(self,  dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        loadUi("VistaDipendente.ui", self)

        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        self.nome_dipendente_label.setText(
            "<font color='white'>" + self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        self.codice_fiscale_label.setText("<font color='white'>Codice Fiscale: " + self.controller.get_cf_dipendente())
        self.data_nascita_label.setText("<font color='white'>Data di Nascita: " + self.controller.get_datanascita_dipendente())
        self.luogo_nascita_label.setText("<font color='white'>Luogo di Nascita: " + self.controller.get_luogonascita_dipendente())
        self.email_label.setText("<font color='white'>Email: " + self.controller.get_email_dipendente())
        self.telefono_label.setText("<font color='white'>Telefono: " + self.controller.get_telefono_dipendente())
        self.licenza_label.setText("<font color='white'>Licenza: " + self.controller.get_licenza_dipendente())

        self.elimina_button.clicked.connect(self.elimina_dipendente_click)

        self.setFixedHeight(534)
        self.setFixedWidth(410)
        self.setWindowTitle(self.controller.get_nome_dipendente())
        self.setWindowIcon(QIcon("icone/accountant2.png"))

    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()