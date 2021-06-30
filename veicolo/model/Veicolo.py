class Veicolo():
    def __init__(self, id, targa, tipo ):
        super(Veicolo, self).__init__()
        self.id = id
        self.targa = targa
        self.tipo = tipo
        self.pagato = None


    def set_pagato(self, pagato):
        self.pagato = pagato





# Da inserire qualcosa, tipo per modificare il pagato?