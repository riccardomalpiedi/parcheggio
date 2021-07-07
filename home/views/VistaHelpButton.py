from PyQt5.QtWidgets import QGridLayout, QWidget, QDialog
from PyQt5.uic import loadUi


class VistaHelpButton(QDialog):
    def __init__(self):
        super(VistaHelpButton, self).__init__()
        loadUi("help.ui", self)
        self.setFixedHeight(522)
        self.setFixedWidth(655)
        self.setWindowTitle("Help")
        self.back_button.clicked.connect(self.go_back_button)

    def go_back_button(self):
        self.close()