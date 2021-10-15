import sys
from PyQt5.QtWidgets import QApplication

# main
from home.views.VistaWelcome import WelcomeScreen

app = QApplication(sys.argv)
welcome = WelcomeScreen()
welcome.setFixedHeight(600)
welcome.setFixedWidth(800)
welcome.setWindowTitle("EasyParking")
welcome.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
