class Dipendente():
    def __init__(self, id, nome, cognome, cf, datanascita, luogonascita, email, telefono,  licenza):
        super(Dipendente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.email = email
        self.telefono = telefono
        self.licenza = licenza
