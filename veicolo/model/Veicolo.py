class Veicolo():
    def __init__(self, id, targa, tipo):
        super(Veicolo, self).__init__()
        self.id = id
        self.targa = targa
        self.tipo = tipo
        self.orario_ingresso = None
        self.entrato_con_prenotazione = False
        self.orario_pagato = None
        self.associato = False
        self.prenotazione = None
        self.posteggio_occupato = None

    def set_orario_pagato(self, orario_pagato):
        self.orario_pagato = orario_pagato

    def set_orario_ingresso(self, orario_ingresso):
        self.orario_ingresso = orario_ingresso

    def set_associato(self, associato):
        self.associato = associato

    def get_associato(self):
        return self.associato

    def add_prenotazione(self, prenotazione):
        self.prenotazione = prenotazione

    def check_prenotazione_scaduta(self):
        if self.prenotazione.is_scaduta():
            self.prenotazione = None
            return True

    def get_prenotazione(self):
        return self.prenotazione

    def elimina_prenotazione(self):
        self.prenotazione = None
