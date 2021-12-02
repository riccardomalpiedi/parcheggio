from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VistaHelpButton(QDialog):
    def __init__(self):
        super(VistaHelpButton, self).__init__()
        loadUi("home/views/VistaHelpButton.ui", self)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowTitle("Help")

        self.back_button.clicked.connect(self.go_back_button)

    def go_back_button(self):
        self.close()
