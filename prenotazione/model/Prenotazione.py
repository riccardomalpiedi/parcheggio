
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

        #     if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
        #         with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
        #             lista_posteggi_salvata = pickle.load(f)
        #         for posteggio in lista_posteggi_salvata:
        #             if posteggio.id == self.posteggio.id:
        #                 posteggio.disponibile = True
        #     return True
        # return False
