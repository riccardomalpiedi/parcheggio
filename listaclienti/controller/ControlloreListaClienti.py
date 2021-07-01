import pickle
import os.path

from listaclienti.model.ListaClienti import ListaClienti


class ControlloreListaClienti():
    def __init__(self):
        super(ControlloreListaClienti, self).__init__()
        self.model = ListaClienti()
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            print("esiste")
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
            self.model = lista_clienti_salvata

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_clienti(self):
        return self.model.get_lista_clienti()

    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    def elimina_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)