
class ControlloreCliente():
    def __init__(self, cliente):
        self.model = cliente

    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def set_nome_cliente(self, nome):
        self.model.nome = nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def set_cognome_cliente(self, cognome):
        self.model.cognome = cognome

    def get_cf_cliente(self):
        return self.model.cf

    def set_cf_cliente(self, cf):
        self.model.cf = cf

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def set_indirizzo_cliente(self, indirizzo):
        self.model.indirizzo = indirizzo

    def get_email_cliente(self):
        return self.model.email

    def set_email_cliente(self, email):
        self.model.email = email

    def get_telefono_cliente(self):
        return self.model.telefono

    def set_telefono_cliente(self, telefono):
        self.model.telefono = telefono

    def get_lista_dei_veicoli(self):
        return self.model.get_lista_veicoli()

    def set_lista_dei_veicoli(self, lista_veicoli):
        self.model.lista_veicoli = lista_veicoli

    def aggiungi_veicolo(self, veicolo):
        self.model.aggiungi_veicolo(veicolo)

    def get_veicolo_by_index(self, index):
        return self.model.get_veicolo_by_index(index)

    def elimina_veicolo_by_id(self, id):
        self.model.rimuovi_veicolo_by_id(id)

    def get_username_cliente(self):
        return self.model.username

    def get_password_cliente(self):
        return self.model.password

    def set_password_cliente(self, password):
        self.model.password = password

    def get_image_cliente(self):
        return self.model.image

    def set_image_cliente(self, image):
        self.model.image = image
