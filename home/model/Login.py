import json
import pickle
import os.path


class Login:

    def __init__(self):
        super(Login, self).__init__()
        self.lista_credenziali = []
        if os.path.isfile('home/data/lista_credenziali_salvate.pickle'):
            with open('home/data/lista_credenziali_salvate.pickle', 'rb') as f:
                self.lista_credenziali = pickle.load(f)
        else:
            with open('home/data/credenziali.json') as f:
                lista_credenziali = json.load(f)
            for credenziali_iniziali in lista_credenziali:
                self.lista_credenziali.append(Credenziali(credenziali_iniziali["id"], credenziali_iniziali["username"],
                                                          credenziali_iniziali["password"]))

    def login_function(self, username, password):
        for credenziali in self.lista_credenziali:
            if username == credenziali.username and password == credenziali.password:
                return credenziali.id
        return None

    def save_data(self):
        with open('home/data/lista_credenziali_salvate.pickle', 'wb') as handle:
            pickle.dump(self.lista_credenziali, handle, pickle.HIGHEST_PROTOCOL)


class Credenziali:
    def __init__(self, id, username, password):
        super(Credenziali, self).__init__()

        self.id = id
        self.username = username
        self.password = password

