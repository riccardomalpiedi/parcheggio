from datetime import datetime


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

    # Questo metodo setta la prenotazione su None se è scaduta
    def check_prenotazione_scaduta(self):
        if self.prenotazione is not None and self.prenotazione.is_scaduta() and not self.entrato_con_prenotazione:
            self.prenotazione = None

    def get_prenotazione(self):
        return self.prenotazione

    def elimina_prenotazione(self):
        self.prenotazione = None

    def calcola_importo_veicolo(self):
        return ((datetime.now() - self.orario_ingresso).seconds // 3600 + 1) * self.posteggio_occupato.tariffa_oraria

    def calcola_importo_prenotazione(self):
        return self.prenotazione.calcola_importo_prenotazione()
