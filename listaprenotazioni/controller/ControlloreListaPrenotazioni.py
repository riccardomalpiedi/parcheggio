import pickle
import os.path

from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class ControlloreListaPrenotazioni():
    def __init__(self):
        super(ControlloreListaPrenotazioni, self).__init__()
        self.model = ListaPrenotazioni()
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                lista_prenotazioni_salvata = pickle.load(f)
            self.model = lista_prenotazioni_salvata

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_delle_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def get_prenotazione_by_index(self, index):
        return self.model.get_prenotazione_by_index(index)

    def elimina_prenotazione_by_id(self, id):
        self.model.rimuovi_prenotazione_by_id(id)
        self.model.disdici_by_id(id)
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)