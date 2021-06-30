from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from posteggio.controller.ControllorePosteggio import ControllorePosteggio


class VistaPosteggio(QWidget):
    def __init__(self, posteggio, parent=None):
        super(VistaPosteggio, self).__init__(parent)
        self.controller = ControllorePosteggio(posteggio)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_nome = QLabel(self.controller.get_nome_posteggio())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        label_tipo = QLabel("Tipo: {}".format(self.controller.get_tipo_posteggio()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(17)
        label_tipo.setFont(font_tipo)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        label_disponibile = QLabel(self.controller.get_posteggio_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(17)
        label_disponibile.setFont(font_disponibile)
        v_layout.addWidget(label_disponibile)
        h_layout.addLayout(v_layout)

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        label_prezzo = QLabel("Prezzo: {}€".format(self.controller.get_prezzo_posteggio()))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(17)
        label_prezzo.setFont(font_prezzo)
        v_layout2.addWidget(label_prezzo)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(posteggio.nome)