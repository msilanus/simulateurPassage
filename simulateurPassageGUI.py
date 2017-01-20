# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulateurPassage.ui'
#
# Created: Fri Jan 20 10:29:01 2017
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(442, 470)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Simulateur de passage", None, QtGui.QApplication.UnicodeUTF8))
        self.spbFreqence = QtGui.QSpinBox(Dialog)
        self.spbFreqence.setGeometry(QtCore.QRect(251, 20, 51, 22))
        self.spbFreqence.setMinimum(1)
        self.spbFreqence.setMaximum(60)
        self.spbFreqence.setObjectName(_fromUtf8("spbFreqence"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 161, 20))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Fréquence de passages (/min) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lePersonnels = QtGui.QLineEdit(Dialog)
        self.lePersonnels.setGeometry(QtCore.QRect(252, 60, 51, 20))
        self.lePersonnels.setText(QtGui.QApplication.translate("Dialog", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.lePersonnels.setObjectName(_fromUtf8("lePersonnels"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 91, 16))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Personnels :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(79, 100, 161, 20))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Points de passages :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spbPointsPassages = QtGui.QSpinBox(Dialog)
        self.spbPointsPassages.setGeometry(QtCore.QRect(250, 100, 51, 22))
        self.spbPointsPassages.setMinimum(1)
        self.spbPointsPassages.setMaximum(20)
        self.spbPointsPassages.setObjectName(_fromUtf8("spbPointsPassages"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 75, 23))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Calculer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lblTempsTotal = QtGui.QLabel(Dialog)
        self.lblTempsTotal.setGeometry(QtCore.QRect(100, 160, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTempsTotal.setFont(font)
        self.lblTempsTotal.setText(QtGui.QApplication.translate("Dialog", "----", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTempsTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTempsTotal.setObjectName(_fromUtf8("lblTempsTotal"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 200, 141, 16))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Temps total de passage :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 431, 251))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("tourniquet.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.calcul)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

