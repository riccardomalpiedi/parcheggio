import os
import pickle
from datetime import date, datetime, time, timedelta

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QDialog):
    def __init__(self, controller):
        super(VistaInserisciPrenotazione, self).__init__()
        loadUi("prenotazione/views/VistaInserisciPrenotazione.ui", self)

        self.controller = controller

        self.comboposteggi_model = QStandardItemModel(self.posteggio_comboBox)
        if os.path.isfile('listaposteggi/data/lista_posteggi_salvata.pickle'):
            with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'rb') as f:
                self.lista_posteggi_salvata = pickle.load(f)
            self.lista_posteggi_disponibili = [s for s in self.lista_posteggi_salvata if s.is_disponibile()]
            for posteggio in self.lista_posteggi_disponibili:
                item = QStandardItem()
                item.setText(posteggio.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboposteggi_model.appendRow(item)
            self.posteggio_comboBox.setModel(self.comboposteggi_model)

        self.calendarWidget.selectionChanged.connect(self.print_date)
        self.ok_button.clicked.connect(self.add_prenotazione_click)

    def print_date(self):
        selected_date = self.calendarWidget.selectedDate()
        font = self.label.font()
        font.setPointSize(10)
        if selected_date >= date.today():
            date_in_string = "<font color='white'>" + str(selected_date.toPyDate())
            self.label.setText(date_in_string)
            self.label.setFont(font)
        else:
            self.label.setText("<font color='white'>" + "no" + str(selected_date.toPyDate()))
            self.label.setFont(font)

    def add_prenotazione_click(self):
        selected_date = self.calendarWidget.selectedDate().toPyDate()
        if selected_date < date.today():
            QMessageBox.critical(self, 'Errore', "La data selezionata non è valida", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if not self.is_number(self.giorni_lineEdit.text()) or int(self.giorni_lineEdit.text()) <= 0:
                QMessageBox.critical(self, 'Errore', "Il numero di giorni selezionato non è valido",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                data_inizio = datetime.combine(selected_date, time())
                selected_days = timedelta(days=int(self.giorni_lineEdit.text()))
                data_fine = (datetime.combine(selected_date, time()) + selected_days)
                posteggio = self.lista_posteggi_disponibili[self.posteggio_comboBox.currentIndex()]
                if posteggio.tipo != self.controller.get_tipo_veicolo() or not posteggio.disponibile:
                    QMessageBox.critical(self, 'Errore', "Il posteggio selezionato non è disponibile",
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return 
                self.controller.add_prenotazione(Prenotazione(self.controller.get_id_veicolo() + "-" + posteggio.id,
                                                              posteggio, data_inizio, data_fine))
                posteggio.disponibile = False
                with open('listaposteggi/data/lista_posteggi_salvata.pickle', 'wb') as f:
                    pickle.dump(self.lista_posteggi_salvata, f, pickle.HIGHEST_PROTOCOL)
                self.close()

    def is_number(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False
