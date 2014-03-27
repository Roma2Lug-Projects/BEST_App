'''
Created on 25/mar/2014

@author: sectumsempra
'''
import sys
#import threading
import pickle

class reader():

    def __init__(self):
        self.lista_nomi = []
        self.lista_pes = []
        self.lista_var = []
        self.mat_punteggi = []



    def nomi(self):
        nom = open('lista_nomi.txt', 'r')
        for line in nom:
            nome = line.rstrip('\n')
            self.lista_nomi.append(nome)
        nom.close()


    def variab(self):
        var = open('lista_var.txt', 'r')
        for line in var:
            variabile = line.rstrip('\n')
            self.lista_var.append(variabile)
        var.close()



    def rpesi(self):
        pes = open('lista_pes.txt', 'r')
        for line in pes:
            peso = line.rstrip('\n')
            self.lista_pes.append(peso)
        pes.close()


    def punteggi(self):
        punt = open('lista_punteggi.txt', 'r')
        for line in punt:
            punt_conc = line.rstrip('\n')
            lista = punt_conc.split('|')

            self.mat_punteggi.append(lista)




class calcoli():

    #def __init__(self, nomi, variabili, pesi, mat_punteggi):
    def __init__(self, dati):
        self.n_conc = len(dati.lista_nomi)
        self.n_var = len(dati.lista_var)
        self.lis_pf = []
        self.divisore = 0
        self.dati = dati

    def divisr(self):
        # for i in self.dati.lista_pes:
        #    a = 1
        self.divisore = 1

    def calc(self):
        for parziali in self.dati.mat_punteggi:
            punteggio = 0
            for index in range(self.n_var):
                pu = int(parziali[index])
                pe = float(self.dati.lista_pes[index])
                pf = pu * pe
                punteggio += pf

            ppf = punteggio / self.divisore
            self.lis_pf.append(ppf)


class output():
    def __init__(self, nomi, lis_pf, lista_var, mat_punteggi, lista_pesi):
        self.ln = len(nomi)
        self.lis_pf_dis = lis_pf
        self.lis_pf_ord = []
        self.nomi = nomi
        self.lista_var = lista_var
        self.mat_punteggi = mat_punteggi
        self.lista_pesi = lista_pesi

    def ordina_liste(self):

        # Creating list of pair (score, team)
        for i in range(self.ln):
            t = (self.lis_pf_dis[i], self.nomi[i])
            self.lis_pf_ord.append(t)

        self.lis_pf_ord.sort()
        self.lis_pf_ord.reverse()

    def scrivi_file(self):
        punteggioni = open('results.bin', 'wb+')

        out = []

        # [ "Squadra", "Param1", "Param2" ... , "Totale" ]

        header = [ [] ]

        header[0].append("Squadra")
        header[0].extend(self.lista_var)
        header[0].append("Totale")

        # out.append(header)
        
        for index, team_name in enumerate(self.nomi):
            row = []
            row.append(team_name)

            # compute values with weight

            punteggi = self.mat_punteggi[index]

            for i in range(len(punteggi)):
                p = float(punteggi[i])*float(self.lista_pesi[i])
                punteggi[i] = "{0:.2f}".format(p)

            row.extend(punteggi)

            row.append(self.lis_pf_dis[index])

            out.append(row)

        out_sorted = sorted(out, key=lambda col: col[-1], reverse=True)

        header.extend(out_sorted)

        print(header)

        pickle.dump(header, punteggioni)

        punteggioni.close()
