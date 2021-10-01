
class ControlloreCliente():
    def __init__(self, cliente):
        self.model = cliente

    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_cf_cliente(self):
        return self.model.cf

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def aggiungi_veicolo(self, veicolo):
        self.model.aggiungi_veicolo(veicolo)

    def get_lista_dei_veicoli(self):
        return self.model.get_lista_veicoli()

    def get_veicolo_by_index(self, index):
        return self.model.get_veicolo_by_index(index)

    def elimina_veicolo_by_id(self, id):
        self.model.rimuovi_veicolo_by_id(id)

    def get_username_cliente(self):
        return self.model.username

    def get_password_cliente(self):
        return self.model.password

    def get_image_cliente(self):
        return self.model.image
