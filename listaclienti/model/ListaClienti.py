import os
import pickle


class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []
        self.lista_veicoli = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            print("esiste")
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                self.lista_veicoli = pickle.load(f)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)
        if cliente.lista_veicoli is not None:
            for veicolo in cliente.lista_veicoli:
                for veicolo_in_lista in self.lista_veicoli:
                    if veicolo_in_lista.id == veicolo.id:
                        veicolo_in_lista.set_associato(True)

    def rimuovi_cliente_by_id(self, id):
        for cliente in self.lista_clienti:
            if cliente.id == id:
                if cliente.lista_veicoli is not None:
                    for veicolo in cliente.lista_veicoli:
                        for veicolo_in_lista in self.lista_veicoli:
                            if veicolo_in_lista.id == veicolo.id:
                                veicolo_in_lista.set_associato(False)
                self.lista_clienti.remove(cliente)
                return True
        return False

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    def get_cliente_by_id(self, id):
        for cliente in self.lista_clienti:
            if cliente.id == id:
                return cliente
        return None

    def get_lista_clienti(self):
        return self.lista_clienti

    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
        with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_veicoli, handle, pickle.HIGHEST_PROTOCOL)
