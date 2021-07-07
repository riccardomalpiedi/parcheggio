class Prenotazione():
    def __init__(self, id, cliente, servizio, datainizio, datafine):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        self.servizio = servizio
        self.datainizio = datainizio
        self.datafine = datafine