class ControlloreVeicolo():

    def __init__(self, veicolo):
        self.model = veicolo

    def get_id_veicolo(self):
        return self.model.id

    def get_targa_veicolo(self):
        return self.model.targa

    def get_tipo_veicolo(self):
        return self.model.tipo

    def get_orario_pagato_veicolo(self):
        return self.model.orario_pagato

    def get_orario_ingresso(self):
        return self.model.orario_ingresso

    def get_entrato_con_prenotazione(self):
        return self.model.entrato_con_prenotazione

    def set_orario_pagato(self, orario_pagato):
        self.model.set_orario_pagato(orario_pagato)

    def set_orario_ingresso(self, orario_ingresso):
        self.model.set_orario_ingresso(orario_ingresso)

    def set_associato(self, associato):
        self.model.associato = associato

    def get_associato(self):
        return self.model.associato

    def add_prenotazione(self, prenotazione):
        self.model.add_prenotazione(prenotazione)

    def get_prenotazione(self):
        return self.model.get_prenotazione()

    def elimina_prenotazione(self):
        self.model.elimina_prenotazione()

    def get_posteggio_occupato(self):
        return self.model.posteggio_occupato

    def check_prenotazione_scaduta(self):
        self.model.check_prenotazione_scaduta()

    def calcola_importo_veicolo(self):
        return self.model.calcola_importo_veicolo()

    def calcola_importo_prenotazione(self):
        return self.model.calcola_importo_prenotazione()