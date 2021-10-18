
class ControllorePrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        return self.model.id

    def get_posteggio_prenotazione(self):
        return self.model.posteggio

    def get_data_inizio_prenotazione(self):
        return self.model.data_inizio

    def get_data_fine_prenotazione(self):
        return self.model.data_fine
