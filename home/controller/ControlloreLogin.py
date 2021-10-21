from home.model.Login import Login


class ControlloreLogin():

    def __init__(self):
        super(ControlloreLogin, self).__init__()
        self.model = Login()

    def login_function(self, username, password):
        return self.model.login_function(username, password)

    def get_id_credenziali(self):
        return self.model1.id

    def get_username_credenziale(self):
        return self.model1.username

    def get_password_credenziale(self):
        return self.model1.password

    def set_password(self, id, password):
        self.model.set_password(id, password)

    def save_data(self):
        self.model.save_data()
