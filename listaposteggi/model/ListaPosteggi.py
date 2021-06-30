import json
import pickle
import os.path

from posteggio.model.Posteggio import Posteggio


class ListaPosteggi():

    def __init__(self):
        super(ListaPosteggi, self).__init__()
        self.lista_posteggi = []
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                self.lista_posteggi = pickle.load(f)
        else:
            with open('listaposteggi/data/lista_posteggi_iniziali.json') as f:
                lista_posteggi_iniziali = json.load(f)
            for posteggio_iniziale in lista_posteggi_iniziali:
                self.aggiungi_posteggio(Posteggio(posteggio_iniziale["id"], posteggio_iniziale["nome"],
                                                posteggio_iniziale["tipo"], posteggio_iniziale["prezzo"]))

    def aggiungi_posteggio(self, posteggio):
        self.lista_posteggi.append(posteggio)

    def get_posteggio_by_index(self, index):
        return self.lista_posteggi[index]

    def get_lista_posteggi(self):
        return self.lista_posteggi

    def save_data(self):
        with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_posteggi, handle, pickle.HIGHEST_PROTOCOL)