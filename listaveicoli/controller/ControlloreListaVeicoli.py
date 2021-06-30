import pickle
import os.path

from listaveicoli.model.ListaVeicoli import ListaVeicoli


class ControlloreListaVeicoli():
    def __init__(self):
        super(ControlloreListaVeicoli, self).__init__()
        self.model = ListaVeicoli()
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            print("esiste")
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                lista_veicoli_salvata = pickle.load(f)
            self.model = lista_veicoli_salvata

    def aggiungi_veicolo(self, veicolo):
        self.model.aggiungi_veicolo(veicolo)
        with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_veicoli(self):
        return self.model.get_lista_veicoli()

    def get_veicolo_by_index(self, index):
        return self.model.get_veicolo_by_index(index)

    def elimina_veicolo_by_id(self, id):
        self.model.rimuovi_veicolo_by_id(id)
        with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)