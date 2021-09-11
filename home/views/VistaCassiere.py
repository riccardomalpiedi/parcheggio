from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.uic import loadUi


from VistaDelCassiere.VistaListaVeicoliDip import VistaListaVeicoliDip
# from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaCassiere(QDialog):
    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        loadUi("Cassiere.ui", self)

        # self.dipendente = dipendente
        # self.controller = ControlloreDipendente(self.dipendente)

        # self.nome_label.setText("Accesso eseguito come " + self.controller.get_nome_dipendente() +
                                # self.controller.get_cognome_dipendente())
        self.lista_veicoli_button.clicked.connect(self.go_vista_lista_veicoli)

        self.setWindowTitle('Vista Cassiere')
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowIcon(QIcon("icone/cash2.png"))

    def go_vista_lista_veicoli(self):
        self.vista_lista_veicoliDip = VistaListaVeicoliDip()
        self.vista_lista_veicoliDip.show()
