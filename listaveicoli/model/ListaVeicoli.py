import os
import pickle


class ListaVeicoli():
    def __init__(self):
        super(ListaVeicoli, self).__init__()
        self.lista_veicoli = []
        if os.path.isfile('listaveicoli/data/lista_veicoli_salvata.pickle'):
            print("esiste")
            with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'rb') as f:
                self.lista_veicoli = pickle.load(f)

    def aggiungi_veicoli(self, veicolo):
        self.lista_veicoli.append(veicolo)

    def rimuovi_veicolo_by_id(self, id):
        for veicolo in self.lista_veicoli:
            if veicolo.id == id:
                self.lista_veicoli.remove(veicolo)
                return True
        return False

    def get_veicolo_by_index(self, index):
        return self.lista_veicoli[index]

    def get_veicolo_by_targa(self, targa):
        for veicolo in self.lista_veicoli:
            if veicolo.targa == targa:
                return veicolo
        return None

    def get_lista_veicoli(self):
        return self.lista_veicoli

    def save_data(self):
        with open('listaveicoli/data/lista_veicoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_veicoli, handle, pickle.HIGHEST_PROTOCOL)
