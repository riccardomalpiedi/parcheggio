from home.model.Login import Login


class ControlloreLogin():

    def __init__(self):
        super(ControlloreLogin, self).__init__()
        self.model = Login()

    def login_function(self, username, password):
        return self.model.login_function(username, password)

    def set_password(self, id, password):
        self.model.set_password(id, password)

    def save_data(self):
        self.model.save_data()
