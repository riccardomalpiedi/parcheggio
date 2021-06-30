class ListaVeicoli():
    def __init__(self):
        super(ListaVeicoli, self).__init__()
        self.lista_veicoli = []

    def aggiungi_veicoli(self, veicolo):
        self.lista_veicoli.append(veicolo)

    def rimuovi_veicolo_by_id(self, id):
        for veicolo in self.lista_veicoli:
            if veicolo.id == id:
                self.lista_veicoli.remove(veicolo)
                return True
        return False

    def get_veicolo_by_index(self, index):
        return self.lista_veicolo[index]

    def get_lista_veicoli(self):
        return self.lista_veicoli