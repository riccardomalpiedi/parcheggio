class ControllorePosteggio():
    def __init__(self, posteggio):
        self.model = posteggio

    def get_nome_posteggio(self):
        return self.model.nome

    def get_tipo_posteggio(self):
        return self.model.tipo

    def get_prezzo_posteggio(self):
        return "{}".format(self.model.prezzo)

    def get_posteggio_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"