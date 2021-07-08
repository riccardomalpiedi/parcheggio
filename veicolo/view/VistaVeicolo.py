from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy


from veicolo.controller.ControlloreVeicolo import ControlloreVeicolo


class VistaVeicolo(QWidget):
    def __init__(self, veicolo, elimina_veicolo, elimina_callback, parent=None):
        super(VistaVeicolo, self).__init__(parent)
        self.controller = ControlloreVeicolo(veicolo)
        self.elimina_veicolo = elimina_veicolo
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_targa = QLabel("veicolo di targa: "+self.controller.get_targa_veicolo())
        font_targa = label_targa.font()
        font_targa.setPointSize(30)
        label_targa.setFont(font_targa)
        v_layout.addWidget(label_targa)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo: {}".format(self.controller.get_tipo_veicolo()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(17)
        label_tipo.setFont(font_tipo)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_veicolo_click)
        v_layout.addWidget(btn_elimina)
        btn_pagamento = QPushButton("Conferma pagamento")
        btn_pagamento.clicked.connect(self.pagamento_veicolo_click)
        v_layout.addWidget(btn_pagamento)

        self.setLayout(v_layout)
        self.setWindowTitle(veicolo.targa)

    def elimina_veicolo_click(self):
        self.elimina_veicolo(self.controller.get_id_veicolo())
        self.elimina_callback()
        self.close()

    def pagamento_veicolo_click(self):
        self.set_pagato(self, True)
