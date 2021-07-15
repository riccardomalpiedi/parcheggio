class Veicolo():
    def __init__(self, id, targa, tipo):
        super(Veicolo, self).__init__()
        self.id = id
        self.targa = targa
        self.tipo = tipo
        self.orario_ingresso = None
        self.pagato = None

    def set_pagato(self, pagato):
        self.pagato = pagato

    def set_orario_ingresso(self, orario_ingresso):
        self.orario_ingresso = orario_ingresso