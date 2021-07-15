class Prenotazione():
    def __init__(self, id, cliente, veicolo, posteggio, data_inizio, data_fine):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        self.veicolo = veicolo
        self.posteggio = posteggio
        self.data_inizio = data_inizio
        self.data_fine = data_fine