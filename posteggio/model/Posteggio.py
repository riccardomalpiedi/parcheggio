class Posteggio():

    def __init__(self, id, nome, tipo, tariffa_oraria, tariffa_giornaliera_prenotazioni):
        super(Posteggio, self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.tariffa_oraria = tariffa_oraria
        self.tariffa_giornaliera_prenotazioni = tariffa_giornaliera_prenotazioni
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False
