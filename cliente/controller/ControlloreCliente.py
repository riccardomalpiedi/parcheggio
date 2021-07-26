import pickle

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

    def get_veicolo_cliente(self):
        return self.model.veicolo

    def get_veicolo2_cliente(self):
        return self.model.veicolo2

    def get_username_cliente(self):
        return self.model.username

    def get_password_cliente(self):
        return self.model.password

    def get_image_cliente(self):
        return self.model.image

    def get_abbonamento_cliente(self):
        return self.model.abbonamento

    def aggiungi_nuovo_abbonamento_cliente(self, abbonamento):
        self.model.add_abbonamento(abbonamento)
