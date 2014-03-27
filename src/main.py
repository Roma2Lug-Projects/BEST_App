import sys
import best
import dinamic_out_table
from PyQt4 import QtGui, QtCore


def main(argv):

    rval = best.reader()
    rval.nomi()
    rval.variab()
    rval.rpesi()
    rval.punteggi()


    calc = best.calcoli(rval)
    calc.divisr()
    calc.calc()

    op = best.output(rval.lista_nomi, calc.lis_pf, rval.lista_var, rval.mat_punteggi, rval.lista_pes)
    op.ordina_liste()
    op.scrivi_file()

    dinamic_out_table.main(argv)


if __name__ == "__main__":
    main(sys.argv)
