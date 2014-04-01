import sys, pickle, os, time
from PyQt4 import QtGui, QtCore
from timeit import timeit
from PyQt4.Qt import QGridLayout


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

    lbl_class = lblPos(65)
    lbl_class.setText("1° Classificato\n\n" + tabResult[1][0] + "\n\n con un punteggio di " + str(tabResult[1][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c1Widget)

    def cascata3():
        c1Widget.hide()
        cWidget.showMaximized()

    c1Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), cascata3)

    grid = QtGui.QGridLayout(c1Widget)
    oro = QtGui.QLabel(c1Widget)#RIGA MODIFICATA
    oro.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/oro.png")) #RIGA MODIFICATA
    grid.addWidget(oro, 0, 0, 1, 5)#RIGA MODIFICATA
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)

    c2Widget = QtGui.QWidget()
    c2Widget.setWindowTitle('Risultati EBEC - Secondo Classificato')

    lbl_class = lblPos(65)
    lbl_class.setText("2° Classificato\n\n" + tabResult[2][0] + "\n\n con un punteggio di " + str(tabResult[2][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c2Widget)

    def cascata2():
        c2Widget.hide()
        c1Widget.showMaximized()

    c2Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), cascata2)

    grid = QtGui.QGridLayout(c2Widget)
    argento = QtGui.QLabel(c2Widget)#RIGA MODIFICATA
    argento.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/argento.png")) #RIGA MODIFICATA
    grid.addWidget(argento, 0, 0, 1, 5)#RIGA MODIFICATA
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)

    c3Widget = QtGui.QWidget()
    c3Widget.setWindowTitle('Risultati EBEC - Terzo Classificato')


    lbl_class = lblPos(50)
    lbl_class.setText("3° Classificato\n\n" + tabResult[3][0] + "\n\n con un punteggio di " + str(tabResult[3][-1]))
    lbl_class.setAlignment(QtCore.Qt.AlignCenter)

    btn_continue = QtGui.QPushButton("Continua ->", c3Widget)

    def cascata1():
        c3Widget.hide()
        c2Widget.showMaximized()

    def cascata0():
        t.stop()
        splim.hide()
        c3Widget.showMaximized()

    c3Widget.connect(btn_continue, QtCore.SIGNAL('clicked()'), cascata1)
    grid = QtGui.QGridLayout(c3Widget)
    bronze = QtGui.QLabel(c3Widget) #RIGA MODIFICATA 
    bronze.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/bronzo.png")) # RIGA MODIFICATA 
    grid.addWidget(bronze, 0, 0, 1, 5) # RIGA MODIFICATA 
    grid.addWidget(lbl_class, 0, 0, 1, 8)
    grid.addWidget(btn_continue, 1, 7, 1, 1)

    pix = QtGui.QPixmap("./img/Splashlogo.png")
    splim = QtGui.QSplashScreen(pix)
    splim.setMask(pix.mask())

    def changeres():
        resolution = QtGui.QDesktopWidget().screenGeometry()
        splim.move((resolution.width() / 2) - (splim.frameSize().width() / 2),
                       (resolution.height() / 2) - (splim.frameSize().height() / 2))
    
    changeres()
    splim.show()
    t = QtCore.QTimer()
    t.setInterval(9000)
    t.start()
    t.timeout.connect(cascata0)

    sys.exit(app.exec_())

if __name__=='__main__':
    main(sys.argv)
