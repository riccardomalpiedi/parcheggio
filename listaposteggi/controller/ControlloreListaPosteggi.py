from listaposteggi.model.ListaPosteggi import ListaPosteggi


class ControlloreListaPosteggi():

    def __init__(self):
        super(ControlloreListaPosteggi, self).__init__()
        self.model = ListaPosteggi()

    def get_lista_dei_posteggi(self):
        return self.model.get_lista_posteggi()

    def get_posteggio_by_index(self, index):
        return self.model.get_posteggio_by_index(index)

    def save_data(self):
        self.model.save_data()
