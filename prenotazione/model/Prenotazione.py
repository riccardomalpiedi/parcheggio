
from datetime import datetime


class Prenotazione():
    def __init__(self, id, posteggio, data_inizio, data_fine):
        super(Prenotazione, self).__init__()
        self.id = id
        self.posteggio = posteggio
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.pagata = False

    def is_scaduta(self):
        return datetime.now() > self.data_fine

    def calcola_importo_prenotazione(self):
        return (self.data_fine - self.data_inizio).days * int(self.posteggio.tariffa_giornaliera_prenotazioni)
