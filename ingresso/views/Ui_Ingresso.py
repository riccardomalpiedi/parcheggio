from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ingresso(object):
    def setupUi(self, Ingresso):
        Ingresso.setObjectName("Ingresso")
        Ingresso.resize(589, 406)
        Ingresso.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.layoutWidget = QtWidgets.QWidget(Ingresso)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 501, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"color: rgb(220, 220, 220)")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"color: rgb(220, 220, 220)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Ingresso)
        QtCore.QMetaObject.connectSlotsByName(Ingresso)

    def retranslateUi(self, Ingresso):
        _translate = QtCore.QCoreApplication.translate
        Ingresso.setWindowTitle(_translate("Ingresso", "Form"))
        self.pushButton.setText(_translate("Ingresso", "Inserisci Ingresso Veicolo"))
        self.pushButton_2.setText(_translate("Ingresso", "Registra Veicolo"))
