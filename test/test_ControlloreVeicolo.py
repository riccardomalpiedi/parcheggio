from datetime import datetime, timedelta
from unittest import TestCase

from posteggio.model.Posteggio import Posteggio
from prenotazione.model.Prenotazione import Prenotazione
from veicolo.model.Veicolo import Veicolo


class TestControlloreVeicolo(TestCase):

    # test dell'aggiunta di una prenotazione
    def test_add_prenotazione(self):
        self.veicolo = Veicolo(id="veicolo_test", targa="1234", tipo="Auto")
        self.assertIsNone(self.veicolo.prenotazione)
        prenotazione = Prenotazione(id="prenotazione_test",
                                    posteggio=Posteggio("posteggio_test", "posteggio1", "Auto", 2, 10),
                                    data_inizio=datetime.now(), data_fine=datetime.now() + timedelta(days=2))
        self.veicolo.add_prenotazione(prenotazione)
        self.assertIsNotNone(self.veicolo.prenotazione)

    # test dell'eliminazione di una prenotazione
    def test_elimina_prenotazione(self):
        self.veicolo = Veicolo(id="veicolo_test", targa="1234", tipo="Auto")
        prenotazione = Prenotazione(id="prenotazione_test",
                                    posteggio=Posteggio("posteggio_test", "posteggio1", "Auto", 2, 10),
                                    data_inizio=datetime.now(), data_fine=datetime.now() + timedelta(days=2))
        self.veicolo.add_prenotazione(prenotazione)
        self.assertIsNotNone(self.veicolo.prenotazione)
        self.veicolo.elimina_prenotazione()
        self.assertIsNone(self.veicolo.prenotazione)

    # check prenotazione scaduta imposta su None la prenotazione se è scaduta. Quando eseguo il metodo e la
    # prenotazione non è scaduta non succede niente
    def test_check_prenotazione_scaduta(self):
        self.veicolo = Veicolo(id="veicolo_test", targa="1234", tipo="Auto")
        prenotazione = Prenotazione(id="prenotazione_test",
                                    posteggio=Posteggio("posteggio_test", "posteggio1", "Auto", 2, 10),
                                    data_inizio=datetime.now(), data_fine=datetime.now() + timedelta(days=2))
        self.veicolo.add_prenotazione(prenotazione)
        self.veicolo.check_prenotazione_scaduta()
        self.assertIsNotNone(self.veicolo.prenotazione)
        self.veicolo.prenotazione.data_fine = datetime.now() - timedelta(days=2)
        self.veicolo.check_prenotazione_scaduta()
        self.assertIsNone(self.veicolo.check_prenotazione_scaduta())

    # calcolo l'importo di un veicolo che è rimasto nel parcheggio per un'ora e mezza, la tariffa oraria del posto è di
    # 2 euro, l'importo deve corrispondere a 4 euro
    def test_calcola_importo_veicolo(self):
        self.veicolo = Veicolo(id="veicolo_test", targa="1234", tipo="Auto")
        self.veicolo.posteggio_occupato = Posteggio(id="posteggio_test", nome="posteggio1", tipo="Auto",
                                                    tariffa_oraria=2, tariffa_giornaliera_prenotazioni=10)
        self.veicolo.orario_ingresso = datetime.now() - timedelta(hours=1.5)
        self.assertIs(self.veicolo.calcola_importo_veicolo(), 4)

    # calcolo l'importo di una prenotazione di 2 giorni, la tariffa giornaliera delle prenotazioni è di 10 euro,
    # l'importo deve corrispondere a 20 euro
    def test_calcola_importo_prenotazione(self):
        self.veicolo = Veicolo(id="veicolo_test", targa="1234", tipo="Auto")
        prenotazione = Prenotazione(id="prenotazione_test",
                                    posteggio=Posteggio(id="posteggio_test", nome="posteggio1", tipo="Auto",
                                                        tariffa_oraria=2, tariffa_giornaliera_prenotazioni=10),
                                    data_inizio=datetime.now(), data_fine=datetime.now() + timedelta(days=2))
        self.veicolo.add_prenotazione(prenotazione)
        self.assertIs(self.veicolo.calcola_importo_prenotazione(), 20)
