#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import libdice
import sys
import csv
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

systemTypes = ['democrazy','dictatorship','aristocracy']

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
    print(str((len(sys.argv)-3)/2))
    print(str(sys.argv[3:]))
    #longvar = ("dice.py "+str((len(sys.argv)-3))+" lin 1 1 1").split()
    longvar = ("dice.py "+str(int((len(sys.argv)-3)/2))+" lin 1 1 1").split()
    libdice.dice(longvar,bezeichner=' '.join(sys.argv[3:]))
    writeCsv(sys.argv)
else:
    print(str(systemTypes)+" ???")

readCsv(sys.argv)


