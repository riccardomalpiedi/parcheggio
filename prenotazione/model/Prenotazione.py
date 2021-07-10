class Prenotazione():
    def __init__(self, id, cliente, posteggio, data_inizio, data_fine):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        self.posteggio = posteggio
        self.data_inizio = data_inizio
        self.data_fine = data_fine