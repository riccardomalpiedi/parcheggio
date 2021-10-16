
from listaveicoli.model.ListaVeicoli import ListaVeicoli


class ControlloreListaVeicoli():
    def __init__(self):
        super(ControlloreListaVeicoli, self).__init__()
        self.model = ListaVeicoli()

    def aggiungi_veicolo(self, veicolo):
        self.model.aggiungi_veicolo(veicolo)

    def get_lista_dei_veicoli(self):
        return self.model.get_lista_veicoli()

    def get_veicolo_by_index(self, index):
        return self.model.get_veicolo_by_index(index)

    def get_veicolo_by_targa(self, targa):
        return self.model.get_veicolo_by_targa(targa)

    def get_veicolo_by_id(self, id):
        return self.model.get_veicolo_by_id(id)

    def elimina_veicolo_by_id(self, id):
        self.model.rimuovi_veicolo_by_id(id)

    def save_data(self):
        self.model.save_data()
