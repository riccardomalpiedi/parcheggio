from PyQt5.QtWidgets import QGridLayout, QWidget, QDialog
from PyQt5.uic import loadUi


class VistaAboutusButton(QDialog):
    def __init__(self):
        super(VistaAboutusButton, self).__init__()
        loadUi("aboutus.ui", self)
        self.back_button.clicked.connect(self.go_back_button)

    def go_back_button(self):
        self.close()