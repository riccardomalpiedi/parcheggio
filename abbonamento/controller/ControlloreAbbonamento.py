import datetime


class ControlloreAbbonamento():
    def __init__(self, abbonamento):
        super(ControlloreAbbonamento, self).__init__()
        self.model = abbonamento

    def is_abbonato(self):
        return self.model is not None

    def get_scadenza_string(self):
        print(self.model.scadenza)
        scadenza_date = datetime.datetime.fromtimestamp(self.model.scadenza)
        return "Scadenza {}/{}/{}".format(scadenza_date.day, scadenza_date.month, scadenza_date.year)