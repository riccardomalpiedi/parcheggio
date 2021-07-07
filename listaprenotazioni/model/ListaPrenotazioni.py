class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.lista_prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def rimuovi_prenotazione_by_id(self, id):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id == id:
                self.lista_prenotazioni.remove(prenotazione)
                return True
        return False

    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def disdici_by_id(self, id):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id == id:
                prenotazione.servizio.disponibile = True
                return True
        return False

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni