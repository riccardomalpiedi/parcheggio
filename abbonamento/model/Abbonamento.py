import time

class Abbonamento():
    def __init__(self, scadenza):
        self.scadenza = scadenza

    def is_scaduto(self):
        return int(time.time()) > self.scadenza