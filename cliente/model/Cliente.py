
class Cliente():
    def __init__(self, id, nome, cognome, cf, indirizzo, email, telefono, veicolo, veicolo2, username, password, image):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono
        self.veicolo = veicolo
        self.veicolo2 = veicolo2
        self.username = username
        self.password = password
        self.image = image
        self.abbonamento = None

    def add_abbonamento(self, abbonamento):
        self.abbonamento = abbonamento

    def get_abbonamento(self):
        if self.abbonamento.is_scaduto():
            self.abbonamento = None
            return None
        else:
            return self.abbonamento
