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

    def set_pagato(self, pagato):
        self.model.set_pagato(pagato)

    def set_orario_ingresso(self, orario_ingresso):
        self.model.set_orario_ingresso(orario_ingresso)

    def set_associato(self, associato):
        self.model.associato = associato

    def get_associato(self):
        return self.model.associato
