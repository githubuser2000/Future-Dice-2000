#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import libdice
import sys
import csv
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
import pickle
import math

systemTypeMaps =  {'strnum' : {'democracy': 0,'dictatorship':2,'aristocracy':4},'numstr':{0:'democracy',2:'dictatorship',4:'aristocracy'}}
systemTypes = systemTypeMaps['numstr'].values()

def writeCsv(data):
    print(str(data))
    with open(data[1]+'.txt', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(data[2:])

def readCsv(data):
    with open(data[1]+'.txt', mode='r') as csv_file:
        rowsuntil = []
        for row in reversed(list(csv.reader(csv_file, delimiter=';'))):
            #print ('; '.join(row))
            rowsuntil += [row]
            if row[0] in systemTypes:
                return rowsuntil
            #print(row[0])


def newSystem(auswahl,argv):
    longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
    people1 = libdice.dice(longvar, werfen=auswahl, uniq_=True, bezeichner=' '.join(argv[3:]))
    people = []
    for someone in people1.out()[1]:
        if type(someone) is tuple:
            people.append(someone[3])
    print(str(sys.argv[0:3]+people))
    writeCsv(sys.argv[0:3]+people)

def voting(userAmount,votes, NumberTooMuch=False):
    aristokratenAmount = math.floor(math.sqrt(len(sys.argv[3:])/3+2))
    print('xx '+str(math.sqrt(len(sys.argv[3:])/3+2)))
    results = {}

    for i in range(userAmount):
        results[i] = 0
    for i,vote in enumerate(votes):
        if NumberTooMuch and aristokratenAmount <= i:
            break
        for i in range(userAmount):
            if int(i) == int(vote):
                print(str(i)+' '+str(vote))
                if not i in results.keys():
                    results[i] = 1
                else:
                    results[i] += 1
    return results


def voting2(argv, NumberTooMuch=False):
        print("voting")
        names = []
        votes = []
        for i,entry in enumerate(argv[3:]):
            if i % 3 == 0:
                names += [entry]
            if i % 3 == 1:
                votes += [entry]
        print(str(names))
        votingResults = voting(len(names), votes, NumberTooMuch)
        print('results: '+str(list(enumerate(names)))+' '+str(votingResults))
        print(str(type(['vote']))+' '+str(type(list(votingResults.values()))))
        value = argv[:3]+list(votingResults.values())
        writeCsv(value)


#def __init__(self,inp,werfen = 2, uniq_ = False, bezeichner : str = "", negativ = False, median = False):
if True:
    app =QApplication(sys.argv)
    #libdice.dice.languages1(app)
    qAppEngin = QQmlApplicationEngine()
    libdice_strlist = [qAppEngin.tr('lin'), qAppEngin.tr('log'), qAppEngin.tr('root'), qAppEngin.tr('poly'), qAppEngin.tr('exp'), qAppEngin.tr('kombi'), qAppEngin.tr('logistic'), qAppEngin.tr('rand'), qAppEngin.tr('gewicht'), qAppEngin.tr('add'), qAppEngin.tr('mul'), qAppEngin.tr("Wuerfelwurf: "),qAppEngin.tr(" (Wuerfelaugen ")]
    blub = [qAppEngin.tr('test')]
    libdice.dice.languages2(libdice_strlist)

auswahl=int((len(sys.argv)-3)/3)

if sys.argv[2] in systemTypes:
#    print(str(sys.argv[3:]))
    newSystem(auswahl, sys.argv)
elif sys.argv[2] in ['revolution']:
    oldsystem = readCsv(sys.argv)[-1][0]
    newsystem = systemTypeMaps['numstr'][(systemTypeMaps['strnum'][oldsystem]+2)%6]
    print(newsystem)
    argv = sys.argv
    argv[2] = newsystem
    newSystem(auswahl, argv)
elif sys.argv[2] in ['vote']:
    historyThisGovernment = readCsv(sys.argv)
    print(historyThisGovernment[-1][0])
    if historyThisGovernment[-1][0] == systemTypeMaps['numstr'][0]:
        voting2(sys.argv)
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][4]: # Aristrokratie
        print("vote in Aristokratie")
        longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(sys.argv[4:]))
        print('out: '+str(hierarchyGame.out()))
        voting2(sys.argv, True)

elif sys.argv[2] in ['next']:
    historyThisGovernment = readCsv(sys.argv)
    print(historyThisGovernment[-1][0])
    if historyThisGovernment[-1][0] == systemTypeMaps['numstr'][2]:
        print("next in hierarchy")
        longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(sys.argv[3:]))
        print('out: '+str(hierarchyGame.out()))
        roledone = hierarchyGame.wuerfeln()[0][0]
        print('out: '+str(roledone))
        hierarchynow=[]
        people = []

        for i,someone in enumerate(sys.argv[3:]):
            if i % 3 == 0:
                people.append(someone)
        print('now: '+str(people))

        for i, user in enumerate(people):
            hierarchynow += [user]
            if i == int(roledone):
                break
        print('now: '+str(hierarchynow))
        value = sys.argv[:3]+hierarchynow
        writeCsv(value)





else:
    print(str(systemTypes)+" ???")

