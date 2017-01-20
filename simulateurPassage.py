#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys 
from PyQt4.QtGui import *
import simulateurPassageGUI
#simulateurPassageGUI est le fichier .py genere par pyuic4

class MainDialog(QDialog,simulateurPassageGUI.Ui_Dialog):
	def __init__(self,parent=None):
		super(MainDialog,self).__init__(parent)
		self.setupUi(self)  

	def calcul(self):
         freq = self.spbFreqence.value()
         nbPointsPassage = self.spbPointsPassages.value()
         personnes = int(str(self.lePersonnels.text()))
         temps = 0.0
         temps = personnes / freq / nbPointsPassage
         
         self.lblTempsTotal.setText(str(temps)+" min") 

            
app=QApplication(sys.argv) 
form=MainDialog()
form.show()
app.exec_()
