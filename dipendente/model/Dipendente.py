class Dipendente():
    def __init__(self, id, nome, cognome, datanascita, luogonascita, cf, telefono, email, licenza):
        super(Dipendente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.cf = cf
        self.telefono = telefono
        self.email = email
        self.licenza = licenza