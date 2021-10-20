from home.model.Login import Login


class ControlloreLogin():

    def __init__(self):
        super(ControlloreLogin, self).__init__()
        self.model = Login()

    def login_function(self, username, password):
        return self.model.login_function(username, password)

    def save_data(self):
        self.model.save_data()
