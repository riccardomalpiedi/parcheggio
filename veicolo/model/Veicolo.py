class Veicolo():
    def __init__(self, id, targa, tipo):
        super(Veicolo, self).__init__()
        self.id = id
        self.targa = targa
        self.tipo = tipo
        self.orario_ingresso = None
        self.orario_pagato = None
        self.associato = False

    def set_orario_pagato(self, orario_pagato):
        self.orario_pagato = orario_pagato

    def set_orario_ingresso(self, orario_ingresso):
        self.orario_ingresso = orario_ingresso

    def set_associato(self, associato):
        self.associato = associato

    def get_associato(self):
        return self.associato
