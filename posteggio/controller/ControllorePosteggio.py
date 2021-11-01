class ControllorePosteggio():
    def __init__(self, posteggio):
        self.model = posteggio

    def get_nome_posteggio(self):
        return self.model.nome

    def get_tipo_posteggio(self):
        return self.model.tipo

    def get_tariffa_oraria_posteggio(self):
        return "{}".format(self.model.tariffa_oraria)

    def get_tariffa_giornaliera_prenotazioni_posteggio(self):
        return "{}".format(self.model.tariffa_giornaliera_prenotazioni)

    def get_posteggio_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"
