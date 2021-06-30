class ControlloreVeicolo():

    def __init__(self, Veicolo):
        self.model = Veicolo

    def get_id_veicolo(self):
        return self.model.id

    def get_targa_veicolo(self):
        return self.model.targa

    def get_tipo_veicolo(self):
        return self.model.tipo

    def get_pagato_veicolo(self):
        return self.model.pagato

