class Posteggio():

    def __init__(self, id, nome, tipo, prezzo):
        super(Posteggio, self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.prezzo = prezzo
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False