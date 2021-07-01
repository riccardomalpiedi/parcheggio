class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente_by_id(self, id):
        for cliente in self.lista_clienti:
            if cliente.id == id:
                self.lista_clienti.remove(cliente)
                return True
        return False

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    def get_lista_clienti(self):
        return self.lista_clienti


    #save