import sys, pickle, os 
from PyQt4 import QtGui, QtCore


class LargeTable(QtGui.QTableWidget):
    def __init__(self, tabResult, numRow, numCol, *args):
        QtGui.QTableWidget.__init__(self, *args)
        self.setStyleSheet("font: 16pt \"DejaVu Serif\";\n "
                        #"QTableWidget {background-color: transparent;}"
                        #"QHeaderView::section {background-color: transparent;}"
                        #"QHeaderView {background-color: transparent;}"
                        #"QTableCornerButton::section {background-color: transparent;}"
                        "background-image: url(./img/logo_orange_transparent.png); background-repeat : no-repeat; background position: bottom;")
        self.setRowCount(numRow-1)
        self.setColumnCount(numCol)
        for index_row in range(1, numRow):
            self.setmyResults(index_row)
        
        for index_col in range(0, numCol):
            for index_row in range(0, numRow-1):
                self.item(index_row, index_col).setTextAlignment(QtCore.Qt.AlignHCenter);

        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(tabResult[0])

    def setmyResults(self, row):
        index = 0
        for elem in tabResult[row]:
            newItem = QtGui.QTableWidgetItem(str(elem))
            newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            self.setItem(row-1, index, newItem)
            index += 1

class lblPos(QtGui.QLabel):
    def __init__(self, pt, *args):
        QtGui.QLabel.__init__(self, *args)
        self.setStyleSheet("font: " + str(pt) + "pt \"DejaVu Serif\";\n "
                        "QTableWidget {background-color: transparent;}"
                        "QHeaderView::section {background-color: transparent;}"
                        "QHeaderView {background-color: transparent;}"
                        "QTableCornerButton::section {background-color: transparent;}")

class labelInPosition(QtGui.QLabel):
    def __init__(self, xinit, yinit, xfin, yfin, *args):
        QtGui.QLabel.__init__(self, *args)
        self.setGeometry(xinit, yinit, xfin, yfin)



def main(args):
    input_tab = open('results.bin', 'rb')
    global tabResult
    tabResult = pickle.load(input_tab)
    numCol = len(tabResult[0])
    numRow = len(tabResult)

    app = QtGui.QApplication(args)
   
    cWidget = QtGui.QWidget()
    
    #cWidget.setStyleSheet("background-image: url(./img/logo_orange.png); background-repeat : no-repeat; background attachment:fixed; background position: center")
    cWidget.setWindowTitle('Risultati EBEC - Classifica completa')
    cWidget.showMaximized()
    
    table = LargeTable(tabResult, numRow, numCol)
    #table.setStyleSheet("background-image: url(./img/logo_orange.png); background-repeat : no-repeat; background position: bottom")

    btn_continue = QtGui.QPushButton("Esci", cWidget)
    
    cWidget.connect(btn_continue, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()')) 

    grid = QtGui.QGridLayout(cWidget)
    #grid.setStyleSheet("background-image: url(./img/logo_orange.png)")
    grid.addWidget(table, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)
    pic = QtGui.QLabel(cWidget)
    pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/BEST_signature_scaled.png"))
    grid.addWidget(pic, 1, 0, 1, 2)
    txtlabel = lblPos(20)
    txtlabel.setText("con la collaborazione del ")
    grid.addWidget(txtlabel, 1, 2, 1, 3)
    lugLogo = QtGui.QLabel(cWidget)
    lugLogo.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/roma2lug_logo.png"))
    grid.addWidget(lugLogo, 1, 5, 1, 2)

    c1Widget = QtGui.QWidget()
    c1Widget.setWindowTitle('Risultati EBEC - Primo Classificato')
    c1Widget.showMaximized()
    
    lbl_class = lblPos(75)
    lbl_class.setText("1° Classificato\n\n" + tabResult[1][0] + "\n\n con un punteggio di " + str(tabResult[1][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c1Widget)
     
    c1Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), QtCore.SLOT('hide()')) 

    grid = QtGui.QGridLayout(c1Widget)
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)
    
    c2Widget = QtGui.QWidget()
    c2Widget.setWindowTitle('Risultati EBEC - Secondo Classificato')
    c2Widget.showMaximized()
    
    lbl_class = lblPos(65)
    lbl_class.setText("2° Classificato\n\n" + tabResult[2][0] + "\n\n con un punteggio di " + str(tabResult[2][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c2Widget)
     
    c2Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), QtCore.SLOT('hide()')) 

    grid = QtGui.QGridLayout(c2Widget)
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)
    
    c3Widget = QtGui.QWidget()
    c3Widget.setWindowTitle('Risultati EBEC - Terzo Classificato')
    c3Widget.showMaximized()
    
    lbl_class = lblPos(50)
    lbl_class.setText("3° Classificato\n\n" + tabResult[3][0] + "\n\n con un punteggio di " + str(tabResult[3][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c3Widget)
     
    c3Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), QtCore.SLOT('hide()')) 

    grid = QtGui.QGridLayout(c3Widget)
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)

    sys.exit(app.exec_())

if __name__=='__main__':
    main(sys.argv)
