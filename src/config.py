'''
Created on 10/mar/2014

@author: sectumsempra
'''
import sys
'''
from variab_conc import  errbox
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSignal, SLOT
from PyQt4.QtCore import pyqtSlot, SIGNAL
from PyQt4.QtGui import QPushButton, QTextEdit, QTableWidgetItem
'''
from PyQt4 import QtGui, QtCore
import signal
import time

var_str = 'string'
nom_str = 'ss'
numvarinp = 'ala'
numconcinp = 'asda'
var_lis = []
nom_lis = []
pes_lis = []
punt_fin_dis = []
punt_fin_ord = []
punt_ordinati = []
class_fin = []
#tabellone = None
tab_pesi = None


class confgui(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        global numvarinp, numconcinp
        bwidget = QtGui.QWidget(self)
        master_columner = QtGui.QVBoxLayout()
        grid = QtGui.QGridLayout()
        toplabel = QtGui.QLabel('Setup')
        button1 =QtGui.QPushButton('Start!', bwidget)
        vbox00 = QtGui.QVBoxLayout()
        numconc = QtGui.QLabel('Num. Concorrenti', bwidget)
        vbox00.addWidget(numconc)
        numconcinp = QtGui.QTextEdit()
        vbox00.addWidget(numconcinp)
        vbox01 = QtGui.QVBoxLayout()
        numvar = QtGui.QLabel('Num. Variabili', bwidget)
        numvarinp = QtGui.QTextEdit()
        vbox01.addWidget(numvar)
        vbox01.addWidget(numvarinp)
        grid.addLayout(vbox00, 0, 0)
        grid.addLayout(vbox01, 0, 1)
        master_columner.addWidget(toplabel)
        master_columner.addLayout(grid)
        master_columner.addWidget(button1)
        bwidget.setLayout(master_columner)
        self.setCentralWidget(bwidget)
        button1.clicked.connect(self.settings)
        numvarinp.textChanged.connect(self.var_to_str)
        numconcinp.textChanged.connect(self.nom_to_str)
        self.resize(600, 400)

    def switchwind(self):
        global varconfig
        self.hide()
        varconfig = valorideipesi()
        print("initdone")
        varconfig.show()
        print("alldonw")



    def settings(self):
        self.varstr_to_list()
        self.nomstr_to_list()
        # time.sleep(5)
        self.switchwind()



    def varstr_to_list(self):
        global var_lis
        global var_str
        var_lis = []
        f = open('lista_var.txt', 'w+')
        a = str(var_str)
        f.write(a)
        f.seek(0, 0)
        for line in f:
            linea = line.rstrip('\n')
            var_lis.append(linea)
        f.close()

    def nomstr_to_list(self):
        global nom_lis
        global nom_str
        nom_lis = []
        f = open ('lista_nomi.txt', 'w+')
        a = str(nom_str)
        f.write(a)
        f.seek(0, 0)
        for line in f:
            linea = line.rstrip('\n')
            nom_lis.append(linea)
            print(nom_lis)
        f.close()

    def nom_to_str(self):
        global nom_str
        nom_str = numconcinp.toPlainText()


    def var_to_str(self):
        global var_str
        var_str = numvarinp.toPlainText()


class maingui(QtGui.QMainWindow):
    #global nom_lis
    #global var_lis
    b = []
    col = []

    def __init__(self):
        global nom_lis, var_lis
        QtGui.QMainWindow.__init__(self)
        bWidget = QtGui.QWidget(self)

        self.len_nom_lis = len(nom_lis)
        self.len_var_lis = len(var_lis)

        self.tabellone = QtGui.QTableWidget()

        self.tabellone.setColumnCount(self.len_var_lis)
        self.tabellone.setRowCount(self.len_nom_lis)
        self.button_save = QtGui.QPushButton("save", bWidget)

        mainlay = QtGui.QVBoxLayout()
        mainlay.addWidget(self.tabellone)
        mainlay.addWidget(self.button_save)
        bWidget.setLayout(mainlay)
        self.setCentralWidget(bWidget)
        self.grid_mk(nom_lis, var_lis)



    def grid_mk(self, rw_names, col_names):
        rw_num = len(rw_names)
        col_num = len(col_names)

        """
        for a in range(col_num):
            for b in range(rw_num):
                aleph = QtGui.QTableWidgetItem(0)
                aleph.setText(str("0"))
                self.tabellone.setItem(b, a, aleph)
        """

        self.tabellone.setHorizontalHeaderLabels(col_names)
        self.tabellone.setVerticalHeaderLabels(rw_names)
        rw_hei = int(700 / rw_num)
        col_wid = int(1024 / col_num)

        for i in range(0, col_num):
            self.tabellone.setColumnWidth(i, 150)
        for j in range(0, rw_num):
            self.tabellone.setRowHeight(j, 50)

        self.button_save.clicked.connect(self.readScores)
        print(rw_hei, col_wid)
        print("finished grid")
        #return None

    def readScores(self):
        global nom_lis
        global var_lis
        righe = len(nom_lis)
        colonne = len(var_lis)
        n = 0

        f = open('lista_punteggi.txt','w+')

        for rig in range(righe):
            punt = []
            for col in range(colonne):
                pnt = str(self.tabellone.item(rig, col).text())
                punt.append(pnt)

            risultati = "|".join(punt)

            f.write(risultati + "\n")

        f.close()

        self.close()

class valorideipesi(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        global var_lis, tab_pesi
        num_r = len(var_lis)
        sWidget = QtGui.QWidget()
        tab_pesi = QtGui.QTableWidget()
        tab_pesi.setColumnCount(1)
        tab_pesi.setRowCount(num_r)
        tab_pesi.setVerticalHeaderLabels(var_lis)
        tab_pesi.setColumnWidth(0, 300)
        for i in range(0, num_r):
            tab_pesi.setRowHeight(i, 80)
        ok = QtGui.QPushButton("OK", sWidget)
        vlay = QtGui.QVBoxLayout()
        vlay.addWidget(tab_pesi)
        vlay.addWidget(ok)
        sWidget.setLayout(vlay)
        self.setCentralWidget(sWidget)
        self.resize(400, 400)
        ok.clicked.connect(self.switchwind1)


    def switchwind1(self):
        global mainwind
        self.saveconstants()
        self.hide()
        mainwind = maingui()
        mainwind.show()
        print("connected")

    def saveconstants(self):
        global var_lis, pes_lis, tab_pesi
        top = len(var_lis)

        for i in range(0, top):
            pes_lis.append(str(tab_pesi.item(i, 0).text())+"\n")

        f = open('lista_pes.txt', 'w+')

        f.writelines(pes_lis)

        f.close()

        print (pes_lis)



def classifica():
    global pes_lis, punt_ordinati, punt_fin_dis, punt_fin_ord, class_fin, nom_lis
    a = len(pes_lis)
    divisore = 0
    for z in pes_lis:
        divisore += int(z)
    top = len(punt_ordinati)

    for lis_n in range (0, top):
        lis = punt_ordinati[lis_n]
        parziali = []
        for i in range(1, a):
            s1 = lis[i]
            s1i = int(s1)
            i2 = i - 1
            s2 = pes_lis[i2]
            s2i = int(s2)
            par = s1i * s2i
            parziali.append(par)
        dividendo = 0
        for x in parziali:
            dividendo += int(x)
        punteggio = float(int(dividendo) / int(divisore))
        punt_fin_dis.append(punteggio)
    punt_fin_ord = punt_fin_dis
    punt_fin_ord.sort()
    max = len(punt_fin_dis)
    for v1 in punt_fin_ord:
        for n in range(0, max):
            if v1 == punt_fin_dis[n]:
                elem = nom_lis[n]
                class_fin.append(elem)
            else: pass

        print(class_fin)
        print(punt_fin_ord)

class myItem(QtGui.QTableWidgetItem):
    def __init__(self):
        QtGui.QTableWidgetItem.__init__(self)
        self.setText("0")

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    config = confgui()

    config.show()

    app.exec_()
