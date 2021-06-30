from listadipendenti.model.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    def elimina_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)

    def save_data(self):
        self.model.save_data()