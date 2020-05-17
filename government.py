#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import libdice
import sys
import csv
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

systemTypes = ['democracy','dictatorship','aristocracy']

def writeCsv(data):
    with open(data[1]+'.txt', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(data[2:])

def readCsv(data):
    with open(data[1]+'.txt', mode='r') as csv_file:
        for row in reversed(list(csv.reader(csv_file, delimiter=';'))):
            print ('; '.join(row))
            if row[0] in systemTypes:
                break
            #print(row[0])

#def __init__(self,inp,werfen = 2, uniq_ = False, bezeichner : str = "", negativ = False, median = False):
if True:
    app =QApplication(sys.argv)
    #libdice.dice.languages1(app)
    qAppEngin = QQmlApplicationEngine()
    libdice_strlist = [qAppEngin.tr('lin'), qAppEngin.tr('log'), qAppEngin.tr('root'), qAppEngin.tr('poly'), qAppEngin.tr('exp'), qAppEngin.tr('kombi'), qAppEngin.tr('logistic'), qAppEngin.tr('rand'), qAppEngin.tr('gewicht'), qAppEngin.tr('add'), qAppEngin.tr('mul'), qAppEngin.tr("Wuerfelwurf: "),qAppEngin.tr(" (Wuerfelaugen ")]
    blub = [qAppEngin.tr('test')]
    libdice.dice.languages2(libdice_strlist)

if sys.argv[2] in systemTypes:
    auswahl=int((len(sys.argv)-3)/3)
    print(str(sys.argv[3:]))
    #longvar = ("dice.py "+str((len(sys.argv)-3))+" lin 1 1 1").split()
    # dice.py 3 gewicht poly 3 2 0.7 -poly 1 2 5
    longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
    people1 = libdice.dice(longvar, werfen=auswahl, uniq_=True, bezeichner=' '.join(sys.argv[3:]))
    people = []
    for someone in people1.out()[1]:
        if type(someone) is tuple:
            people.append(someone[3])
    print(str(sys.argv[0:3]+people))
    writeCsv(sys.argv[0:3]+people)
else:
    print(str(systemTypes)+" ???")

readCsv(sys.argv)


