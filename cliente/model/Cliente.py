
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
        self.lista_veicoli = [veicolo, veicolo2]
        self.username = username
        self.password = password
        self.image = image
        self.abbonamento = None

    def aggiungi_veicolo(self, veicolo):
        self.lista_veicoli.append(veicolo)

    def rimuovi_veicolo_by_id(self, id):
        for veicolo in self.lista_veicoli:
            if veicolo.id == id:
                self.lista_veicoli.remove(veicolo)
                return True
        return False

    def get_veicolo_by_index(self, index):
        return self.lista_veicoli[index]

    def get_lista_veicoli(self):
        return self.lista_veicoli

    def add_abbonamento(self, abbonamento):
        self.abbonamento = abbonamento

    def get_abbonamento(self):
        if self.abbonamento.is_scaduto():
            self.abbonamento = None
            return None
        else:
            return self.abbonamento
