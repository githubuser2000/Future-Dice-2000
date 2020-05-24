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
import random


systemTypeMaps =  {'strnum' : {'democracy': 0, 'plutocracy' : 1, 'dictatorship' : 2, 'tyrannis': 3, 'aristocracy' : 4, 'oligarchy' : 5},'numstr':{0:'democracy',1:'plutocracy',2:'dictatorship',3:'tyrannis',4:'aristocracy',5:'oligarchy'}}
systemTypes = systemTypeMaps['numstr'].values()

def writeCsv(data):
    print(str(data))
    with open(data[1]+'.txt', mode='a+') as csv_file:
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

namesNotAllDifferent = False

def orderOfPrecedence(argv, differentOrder):
    global namesNotAllDifferent
    #print(str(argv[3:]))
    #print(differentOrder)
    users = []
    usernames = []
    for user in differentOrder:
        three = []
        for i,thing in enumerate(argv[3:]):
            if i % 3 == 0 and thing == user:
                three += [thing]
                usernames += [thing]
            if i % 3 == 1 and len(three) == 1:
                three += [thing]
            if i % 3 == 2 and len(three) == 2:
                three += [thing]
                users += [three]
    #print(str(lenset(usernames)))
    if len(set(usernames)) != len(set(differentOrder)):
        namesNotAllDifferent = True

    threes = []
    for three in users:
        threes += three

    #print(threes)
    return threes


#def whoIsNotVotedAnymore(argv, whoNot):
#    allLastVotesAndGovernment = readCsv(sys.argv)
#    government = allLastVotesAndGovernment[-1][1:]
#    names = []
#    for oneNot in whoNot:
#        names += [government[oneNot]]



whoHasMax = set()

def peopleAlreadyDemocraticOrRandomlySelectedInPast(ObjDice=None):
    global whoHasMax
    print("peopleAlreadyDemocraticOrRandomlySelectedInPast")
    for choice in readCsv(sys.argv)[:-1]:
        if choice[0] == 'next':
            ObjDice.wuerfelAugenSet.add(len(choice)-2)
            print("last "+ str(len(choice)-2))
            whoHasMax.add(len(choice)-2)
        elif choice[0] == 'vote':
            maxval = 0
            print(choice)
            for oneCandidateVoteAmount in choice[1:]:
                if maxval < int(oneCandidateVoteAmount):
                    maxval = int(oneCandidateVoteAmount)
            for i, oneCandidateVoteAmount in enumerate(choice[1:]):
                #print('max='+str(oneCandidateVoteAmount))
                if int(maxval) == int(oneCandidateVoteAmount):
                    whoHasMax.add(i)
                    #ObjDice.wuerfelAugenSet.add(i)
                    print("last "+ str(i))
    return whoHasMax




def newSystem(auswahl, argv, oldsystem=systemTypeMaps['numstr'][3]):
    if systemTypeMaps['strnum'][oldsystem] % 2 == 1:
        longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        people1 = libdice.dice(longvar, werfen=auswahl, uniq_=True, bezeichner=' '.join(argv[3:]))
        people1 = people1.out()[1]
        people = []
        for someone in people1:
            if type(someone) is tuple:
                people.append(someone[3])
    else:
        people = readCsv(sys.argv)[-1][1:]

    print(str(sys.argv[0:3]+people))
    writeCsv(sys.argv[0:3]+people)

def voting(userAmount, votes, aristrokratsAreLessThanAll=False, potentials=None, voteHierarchy=0, oligarchy=False):
    global whoHasMax
    aristokratenAmount = math.floor(math.sqrt(len(sys.argv[3:])/3+2))
    results = {}
    if userAmount == len(whoHasMax):
        revolution()
        for l in range(userAmount):
            results[l] = 0
        return results

    for i in range(userAmount):
        results[i] = 0
    for k,(vote,potential) in enumerate(zip(votes,potentials)):
        if aristrokratsAreLessThanAll and aristokratenAmount <= k:
            break
        for i in range(userAmount):
            if int(i) == int(vote):
                if voteHierarchy == 0 or \
                    ( voteHierarchy > 0 and voteHierarchy - 1 <= i) or \
                    ( voteHierarchy < 0 and -voteHierarchy - 1 >= i):
                    if not i in whoHasMax:
                        #if oligarchy and i == k:
                        #    potential = int(oligarchy) * 3
                        if not i in results.keys():
                            results[i] = 1 * int(potential)
                        else:
                            results[i] += 1 * int(potential)
    isNotZero = 0
    for result in results.values():
        print('asd '+str(result))
        if int(result) != 0:
            isNotZero += 1
    if isNotZero == 0:
        revolution()
    return results


def voting2(argv, aristrokratsAreLessThanAll=False,Plutocracy=False,voteHierarchy=0,oligarchy=False):
        print("voting")
        names = []
        votes = []
        potentials = []
        for i,entry in enumerate(argv[3:]):
            if i % 3 == 0:
                names += [entry]
            if i % 3 == 1:
                votes += [entry]
            if i % 3 == 2:
                potentials += [entry]
        #print(str(names))
        #print("iuz :"+str(len(names))+" "+str(votes)+" "+str(aristrokratsAreLessThanAll)+" "+str(potentials))
        votingResults = voting(len(names), votes, aristrokratsAreLessThanAll,potentials,voteHierarchy,oligarchy)
        #print('results: '+str(list(enumerate(names)))+' '+str(votingResults))
        #print(str(type(['vote']))+' '+str(type(list(votingResults.values()))))
        value = argv[:3]+list(votingResults.values())
        return value

def hierarchy(argv, auswahl):
        print("next in hierarchy")
        systempeople = readCsv(sys.argv)[-1][1:] # Menschen in ihrer Reihenfolge, wie sie vom System anfangs festgelegt wurden
        # in argv stehen die aktuelleren people drin und anders drin, d.h. mit 2
        # zahlen in arrayelementen jeweils
        longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(argv[3:]))
        peopleAlreadyDemocraticOrRandomlySelectedInPast(hierarchyGame)
        print('dice out: '+str(hierarchyGame.out()))
        roledone = hierarchyGame.wuerfeln()[0][0]
        print('roledone: '+str(roledone))

        hierarchynow = []
        flag = False

        for systemman in systempeople:
            for i,nowSomeone in enumerate(argv[3:]):
                if i % 3 == 0 and systemman == nowSomeone:
                    hierarchynow += [nowSomeone]
                    flag = True
                if flag and i % 3 == 1:
                    hierarchynow += [nowSomeone]
                if flag and i % 3 == 2:
                    hierarchynow += [nowSomeone]
                    flag = False

        print('hierarchynow: '+str(hierarchynow))
        if argv[3:][roledone*3] in systempeople:

            hierarchynow = hierarchynow[0:((roledone+1)*3)]
#            for i, user in enumerate(systempeople):
 #               hierarchynow += [user]
 #               if user == argv[3:][roledone]:
 #                   break
            print('hierarchynow: '+str(hierarchynow))
            #endOfEveryVote(roledone,hierarchyGame)
            return hierarchynow

def revolution():
    # von Demokratie auf Plutokratie
    # von x modulo 2 = 0 auf darauf folgendes x += 1
    # von modulo 2 = 1 auf irgendein anderes x modulo 2 = 0
    # aber nicht das, was das entsprechende x modulo 2 = 0 wäre das davor liegen
    # würde
    oldsystem = readCsv(sys.argv)[-1][0]
    print('oldsystem: '+str(systemTypeMaps['strnum'][oldsystem]))
    if systemTypeMaps['strnum'][oldsystem] % 2 == 0:
        print('mod == 0')
        newsystem = systemTypeMaps['numstr'][(systemTypeMaps['strnum'][oldsystem]+1)%6]
    else:
        print('mod == 1')
        randbool = random.randint(0, 1) # randint 0 1 macht 0 oder 1 möglich
        newsystem = systemTypeMaps['numstr'][(systemTypeMaps['strnum'][oldsystem]+1+(2*randbool))%6]
    print(newsystem)
    argv = sys.argv
    argv[2] = newsystem
    newSystem(auswahl, argv, oldsystem)

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
    revolution()
elif sys.argv[2] in ['vote']:
    historyThisGovernment = readCsv(sys.argv)
    argv = sys.argv
    argv= argv[:3] + orderOfPrecedence(argv,historyThisGovernment[-1][1:])
    print(str(argv))
    whoHasMax = peopleAlreadyDemocraticOrRandomlySelectedInPast()

    if namesNotAllDifferent == True:
        print("Some names are equal. Exit!")
        exit()
    #for whoNotAnymore in whoHasMax:
    #    print(argv[whoNotAnymore*3+4])
    #    argv[whoNotAnymore*3+4] = -abs(int(argv[whoNotAnymore*3+4]))
    #print(argv)
    #print(historyThisGovernment[-1][0])

    if historyThisGovernment[-1][0] == systemTypeMaps['numstr'][0]: # Demokratie
        value = voting2(argv)
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][4]: # Aristrokratie
        print("vote in Aristokratie")
        #longvar = ("dice.py "+str(auswahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        #hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(sys.argv[4:]))
        #print('out: '+str(hierarchyGame.out()))
        value = voting2(argv, True)
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][1]: # Plutokratie
        value = voting2(argv, False, True)
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][5]: # Oligarchie - Programmiere ich später - mehr Eigennutz der Chefs, d.h. normale Wahl und dürfen bei jedem zweiten Mal selbst
#def voting2(argv, aristrokratsAreLessThanAll=False,Plutocracy=False,voteHierarchy=0,oligarchy=False):
        value = voting2(argv, True, False, 0, True)
#    if value[2] == 'vote':
 #       writeCsv(value)
#
#elif sys.argv[2] in ['next']:  # Tyranei und Dictatorship: beides Hierarchie, aber jeder der dran ist hat die Wahl sich oder höher bei Tyranei oder sich oder niedriger bei Dictatorship
#    historyThisGovernment = readCsv(sys.argv)
#    print(historyThisGovernment[-1][0])
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][2]: # Dictatorship
        value = hierarchy(argv, auswahl)
        print('val: '+str(value))
        print('blub: '+ str(argv[:3] + value))
        value = voting2(argv[:3] + value, False, False, int(len(value)/3))
    elif historyThisGovernment[-1][0] == systemTypeMaps['numstr'][3]: # Tyranei
        value = hierarchy(argv, auswahl)
        print('val: '+str(value))
        print('blub: '+ str(argv[:3] + value))
        value = voting2(argv[:3] + value, False, False, -int(len(value)/3))

    summ = 0
    for val in value[3:]:
        if val != 0:
            summ += 1
    if summ != 0:
        writeCsv(value)

else:
    print(str(systemTypes)+" ???")

