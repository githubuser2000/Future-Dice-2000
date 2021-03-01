#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import math
import os
import pickle
import random
import sys

import libdice
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

# example
# ./government.py x vote b 0 1 c 1 1 e 2 1; tail -5 x.txt
# ./government.py x democracy b 1 c 3 e 21
# 0. python exe, 1. logfile, 2. befehl, 3. 3-5 und 6-8 = erste beiden tripel: name zahl zahl, name zahl zahl
# name zahl zahl entspricht den Parametern vom dice und zwar person, würfelaugenersatzwert und Gewichtung
# befehle können sein: vote, revolution, staatsformname 


# x.txt
# democracy;c;e;b
# staatssystem und 3 Teilnehmer, ggf. als Rangfolge
# danach voten oder next (next bei keine Demokratie-Elemente)
# das ist alles

# next;2;2;2
# vote;1;2;3

systemTypeMaps = {
    "strnum": {
        "democracy": 0,
        "plutocracy": 1,
        "dictatorship": 2,
        "tyrannis": 3,
        "aristocracy": 4,
        "oligarchy": 5,
    },
    "numstr": {
        0: "democracy",
        1: "plutocracy",
        2: "dictatorship",
        3: "tyrannis",
        4: "aristocracy",
        5: "oligarchy",
    },
    "strstr": {
        "democracy": "democracy",
        "plutocracy": "plutocracy",
        "dictatorship": "dictatorship",
        "tyrannis": "tyrannis",
        "aristocracy": "aristocracy",
        "oligarchy": "oligarchy",
    },
}
systemTypes = systemTypeMaps["numstr"].values()

argv = sys.argv


def writeCsv(data):
    """
    schreibt in datei aus parameter 1
    schreibt alles als ;-List ab Parameter 2 in die txt logdatei
    """
    print(str(data))
    with open(data[1] + ".txt", mode="a+") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(data[2:])


def readCsv(data):
    """
    liest rückwärts datei dessen name aus Parameter 1
    list so lange bis die spalte[0] irgend ein Staatssystem im Namen trägt
    Dann wird returned: matrix aus Spalten + Zeilen vom ende bis zum letzten Staatssystem
    """
    with open(data[1] + ".txt", mode="r") as csv_file:
        rowsuntil = []
        for row in reversed(list(csv.reader(csv_file, delimiter=";"))):
            # print ('; '.join(row))
            rowsuntil += [row]
            if row[0] in systemTypes:
                return rowsuntil
            # print(row[0])


namesNotAllDifferent = False


def orderOfPrecedence(argv, differentOrder):
    global namesNotAllDifferent
    """ gibt tripelliste zurück, in gleicher Reihenfolge
    nichts besonderes!

    alle usernamen werden durchgegangen
    wenn vorhandener user und parameteruser gleich ist
    dann in user_name_list
    wenn letzte zahl des tripels der tripel
    dann users_list ein tripel anhängen
    users_list wird returned als variable threes
    """
    # print(str(argv[3:]))
    # print(differentOrder)
    users = []
    usernames = []
    for user in differentOrder:
        three = []
        for i, thing in enumerate(argv[3:]):
            if i % 3 == 0 and thing == user:
                three += [thing]
                usernames += [thing]
            if i % 3 == 1 and len(three) == 1:
                three += [thing]
            if i % 3 == 2 and len(three) == 2:
                three += [thing]
                users += [three]
    # print(str(lenset(usernames)))
    if len(set(usernames)) != len(set(differentOrder)):
        namesNotAllDifferent = True

    threes = []
    for three in users:
        threes += three

    # print(threes)
    return threes


# def whoIsNotVotedAnymore(argv, whoNot):
#    allLastVotesAndGovernment = readCsv(argv)
#    government = allLastVotesAndGovernment[-1][1:]
#    names = []
#    for oneNot in whoNot:
#        names += [government[oneNot]]


whoHasMax = set()


def peopleAlreadyDemocraticOrRandomlySelectedInPast(ObjDice=None):
    global whoHasMax
    print("peopleAlreadyDemocraticOrRandomlySelectedInPast")
    for choice in readCsv(argv)[:-1]:
        """ letzte zeile aus log txt
            die nummer des letzten wird bei whoHasMax angefügt, bei next
            und bei vote ist es die nummer mit der höchsten zahl
            das ist alles, außer dass dice das auch bekommt, bei next nur
        """
        if choice[0] == "next":
            amountPeopleMinusOne =len(choice) - 2 
            ObjDice.wuerfelAugenSet.add(amountPeopleMinusOne)
            print("last " + str(amountPeopleMinusOne)
            whoHasMax.add(amountPeopleMinusOne)
        elif choice[0] == "vote":
            maxval = 0
            print(choice)
            for oneCandidateVoteAmount in choice[1:]:
                if maxval < int(oneCandidateVoteAmount):
                    maxval = int(oneCandidateVoteAmount)
            for i, oneCandidateVoteAmount in enumerate(choice[1:]):
                # print('max='+str(oneCandidateVoteAmount))
                if int(maxval) == int(oneCandidateVoteAmount):
                    whoHasMax.add(i)
                    # ObjDice.wuerfelAugenSet.add(i)
                    print("last " + str(i))
    return whoHasMax


def twistGewichtung(argv):
    """
    Die Gewichtung pro Person wird in ihrer Reihenfolge umgekehrt, so dass der Stärkste und Schwächste umgekehrt stark sind
    """
    argv2 = argv[3:]
    argreverse = argv2.copy()
    argreverse.reverse()
    argreverse2 = argreverse.copy()
    for i, (a, b) in enumerate(zip(argreverse2, argv2)):
        if i % 3 == 0:
            argreverse[i + 2] = argv2[i + 2]
        if i % 3 == 2:
            argreverse[i - 2] = a
    # print(str(argreverse))
    return argv[:3] + argreverse


def newSystem(personenAnzahl, argv, oldsystem=systemTypeMaps["numstr"][3]):
    """
    Bei einem neuen System wird immer der schwächste zum größten und der größte zum kleinsten
    durch die Funktion twistGewichtung
    """
    # print('dd '+str(argv))
    newargv = twistGewichtung(argv)
    # print('ww'+str(newargv))
    if systemTypeMaps["strnum"][oldsystem] % 2 == 1:
        """D.h. wenn es ein böses System ist (modulo 2 == 1), bzw. die 3 verschärften Systeme von den 6! """
        longvar = (
            "dice.py " + str(personenAnzahl) + " gewicht lin 1 1 1 lin 1 1 1"
        ).split()
        """ lineares bzw. genauer konstantes wachstum, also kein wachstum und gewicht auch also gleiches gewicht von allem
        d.h. 6 würfelaugen bedeutet stinknormaler würfel in dem fall, würfelaugen == personenAnzahl"""
        people1 = libdice.dice(
            longvar, werfen=personenAnzahl, uniq_=True, bezeichner=" ".join(newargv[3:])
        )
        """ people1 ergibt sich aus würfelung der alten people aber nur in anderer Reihenfogle """
        print(str(people1.out()))
        people1 = people1.out()[1]
        people = []
        for someone in people1:
            if type(someone) is tuple:
                people.append(someone[3])
    else:
        """
        wenn es zu den nicht bösen 3 varianten: modulo 2 = 0 gehört:
        people werden aus dem letzten system übernommen
        """
        # print("nein")
        people = readCsv(newargv)[-1][1:]

    print(str(newargv[0:3] + people))
    """
    eine Zeile in txt logfile: staatsystemname und die n user mit ihrem namen nach ihrer Rangfolge
    das ist alles, keine zahlen oder so
    """
    writeCsv(newargv[0:3] + people)


def voting(
    userAmount,
    votes,
    aristrokratsAreLessThanAll=False,
    potentials=None,
    voteHierarchy=0,
    oligarchy=False,
):
    global whoHasMax
    aristokratenAmount = math.floor(math.sqrt(len(argv[3:]) / 3 + 2)) # ein oberer Bruchteil ist Aristrokrat
    results = {}
    """ Revolution, wenn alle durch sind und dann alle votes=0 returnen, ende"""
    if userAmount == len(whoHasMax):
        revolution(argv)
        for l in range(userAmount):
            results[l] = 0
        return results

    """ zunächst sind alle votes 0"""
    for i in range(userAmount):
        results[i] = 0
    """
    + bei weniger als alle aristrokaten, stopp, so dass dann nur die aristrokraten wählen
    + for votes for user, d.h. jeder user votet jeden user, es sei denn Aristrokratie
    + """
    for k, (vote, potential) in enumerate(zip(votes, potentials)):
        if aristrokratsAreLessThanAll and aristokratenAmount <= k:
            break
        for i in range(userAmount):
            if int(i) == int(vote):
                """ voteHierarchy definiert sich daraus welche user voten dürfen - das ist alles
                + der max user fällt immer weg, der user mit der nummer whoHasMax
                + in Oligarchie haben user dreifaches potential
                    aber int(boolwert) * 3 ist irgendwie komisch aber funktionierend programmiert
                + wo kommt eigentlich potentials her? 
                + if true oder false, immer: resultliste hat immer den wert 1 * potentialvariable
                """
                if (
                    voteHierarchy == 0
                    or (voteHierarchy > 0 and voteHierarchy - 1 <= i)
                    or (voteHierarchy < 0 and -voteHierarchy - 1 >= i)
                ):
                    if not i in whoHasMax:
                        if oligarchy and i == k:
                            potential = int(oligarchy) * 3
                        if not i in results.keys():
                            results[i] = 1 * int(potential)
                        else:
                            results[i] += 1 * int(potential)

    """ revolution nach vote, wenn es letzter vote war
    + immer returnen der Potentialliste per i = user"""
    isNotZero = 0
    for result in results.values():
        print("asd " + str(result))
        if int(result) != 0:
            isNotZero += 1
    if isNotZero == 0:
        revolution(argv)
    return results


def voting2(
    argv,
    aristrokratsAreLessThanAll=False,
    Plutocracy=False,
    voteHierarchy=0,
    oligarchy=False,
):
    """ tripel in liste, dann vote()
    dann dessen ergebnis returned, einzelne, keine tripel
    aber davor noch die 3 ersten parameter, wozu wohl auch die py datei gehört
    das als liste returned
    """
    print("voting")
    names = []
    votes = []
    potentials = []
    for i, entry in enumerate(argv[3:]):
        if i % 3 == 0:
            names += [entry]
        if i % 3 == 1:
            votes += [entry]
        if i % 3 == 2:
            potentials += [entry]
    # print(str(names))
    # print("iuz :"+str(len(names))+" "+str(votes)+" "+str(aristrokratsAreLessThanAll)+" "+str(potentials))
    votingResults = voting(
        len(names),
        votes,
        aristrokratsAreLessThanAll,
        potentials,
        voteHierarchy,
        oligarchy,
    )
    # print('results: '+str(list(enumerate(names)))+' '+str(votingResults))
    # print(str(type(['vote']))+' '+str(type(list(votingResults.values()))))
    value = argv[:3] + list(votingResults.values())
    return value


def hierarchy(argv, personenAnzahl):
    print("next in hierarchy")
    systempeople = readCsv(argv)[-1][
        1:
    ]  # Menschen in ihrer Reihenfolge, wie sie vom System anfangs festgelegt wurden
    # in argv stehen die aktuelleren people drin und anders drin, d.h. mit 2
    # zahlen in arrayelementen jeweils: name, wert der Augen , gewichtung
    longvar = (
        "dice.py " + str(personenAnzahl) + " gewicht lin 1 1 1 lin 1 1 1"
    ).split()
    hierarchyGame = libdice.dice(
        longvar, werfen=0, uniq_=True, bezeichner=" ".join(argv[3:])
    )
    peopleAlreadyDemocraticOrRandomlySelectedInPast(hierarchyGame)
    print("dice out: " + str(hierarchyGame.out()))
    roledone = hierarchyGame.wuerfeln()[0][0]
    print("roledone: " + str(roledone))

    hierarchynow = []
    flag = False

    for systemman in systempeople:
        for i, nowSomeone in enumerate(argv[3:]):
            if i % 3 == 0 and systemman == nowSomeone:
                hierarchynow += [nowSomeone]
                flag = True
            if flag and i % 3 == 1:
                hierarchynow += [nowSomeone]
            if flag and i % 3 == 2:
                hierarchynow += [nowSomeone]
                flag = False

    print("hierarchynow: " + str(hierarchynow))
    if argv[3:][roledone * 3] in systempeople:

        hierarchynow = hierarchynow[0 : ((roledone + 1) * 3)]
        #            for i, user in enumerate(systempeople):
        #               hierarchynow += [user]
        #               if user == argv[3:][roledone]:
        #                   break
        print("hierarchynow: " + str(hierarchynow))
        # endOfEveryVote(roledone,hierarchyGame)
        return hierarchynow


def revolution(argv):
    # von Demokratie auf Plutokratie
    # von x modulo 2 = 0 auf darauf folgendes x += 1
    # d.h. von einem der guten 3 auf das böse immer
    # von modulo 2 = 1 auf irgendein anderes x modulo 2 = 0
    # aber nicht das, was das entsprechende x modulo 2 = 0 wäre das davor liegen
    # d.h. von etwas bösem auf ein anderes gutes, aber nicht dessen gutes, sondern etwas neues
    # würde
    oldsystem = readCsv(argv)[-1][0]
    print("oldsystem: " + str(systemTypeMaps["strnum"][oldsystem]))
    if systemTypeMaps["strnum"][oldsystem] % 2 == 0:
        print("mod == 0")
        newsystem = systemTypeMaps["numstr"][
            (systemTypeMaps["strnum"][oldsystem] + 1) % 6
        ]
    else:
        print("mod == 1")
        randbool = random.randint(0, 1)  # randint 0 1 macht 0 oder 1 möglich
        newsystem = systemTypeMaps["numstr"][
            (systemTypeMaps["strnum"][oldsystem] + 1 + (2 * randbool)) % 6
        ]
    print(newsystem)
    argv[2] = newsystem
    newSystem(personenAnzahl, argv, oldsystem)


# def __init__(self,inp,werfen = 2, uniq_ = False, bezeichner : str = "", negativ = False, median = False):
if True:
    app = QApplication(argv)
    # libdice.dice.languages1(app)
    qAppEngin = QQmlApplicationEngine()
    libdice_strlist = [
        qAppEngin.tr("lin"),
        qAppEngin.tr("log"),
        qAppEngin.tr("root"),
        qAppEngin.tr("poly"),
        qAppEngin.tr("exp"),
        qAppEngin.tr("kombi"),
        qAppEngin.tr("logistic"),
        qAppEngin.tr("rand"),
        qAppEngin.tr("gewicht"),
        qAppEngin.tr("add"),
        qAppEngin.tr("mul"),
        qAppEngin.tr("Wuerfelwurf: "),
        qAppEngin.tr(" (Wuerfelaugen "),
    ]
    blub = [qAppEngin.tr("test")]
    libdice.dice.languages2(libdice_strlist)

personenAnzahl = int((len(argv) - 3) / 3)

if argv[2] in systemTypes:
    #    print(str(argv[3:]))
    newSystem(personenAnzahl, argv)
elif argv[2] in ["revolution"]:
    revolution(argv)
elif argv[2] in ["vote"]:
    historyThisGovernment = readCsv(argv)
    argv = argv[:3] + orderOfPrecedence(argv, historyThisGovernment[-1][1:])
    print(str(argv))
    whoHasMax = peopleAlreadyDemocraticOrRandomlySelectedInPast()

    if namesNotAllDifferent == True:
        print("Some names are equal. Exit!")
        exit()
    # for whoNotAnymore in whoHasMax:
    #    print(argv[whoNotAnymore*3+4])
    #    argv[whoNotAnymore*3+4] = -abs(int(argv[whoNotAnymore*3+4]))
    # print(argv)
    # print(historyThisGovernment[-1][0])

    if historyThisGovernment[-1][0] == systemTypeMaps["numstr"][0]:  # Demokratie
        value = voting2(argv)
    elif historyThisGovernment[-1][0] == systemTypeMaps["numstr"][4]:  # Aristrokratie
        print("vote in Aristokratie")
        # longvar = ("dice.py "+str(personenAnzahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        # hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(argv[4:]))
        # print('out: '+str(hierarchyGame.out()))
        value = voting2(argv, True)
    elif historyThisGovernment[-1][0] == systemTypeMaps["numstr"][1]:  # Plutokratie
        value = voting2(argv, False, True)
    elif (
        historyThisGovernment[-1][0] == systemTypeMaps["numstr"][5]
    ):  # Oligarchie - Programmiere ich später - mehr Eigennutz der Chefs, d.h. normale Wahl und dürfen bei jedem zweiten Mal selbst
        # def voting2(argv, aristrokratsAreLessThanAll=False,Plutocracy=False,voteHierarchy=0,oligarchy=False):
        value = voting2(argv, True, False, 0, True)
    #    if value[2] == 'vote':
    #       writeCsv(value)
    #
    # elif argv[2] in ['next']:  # Tyranei und Dictatorship: beides Hierarchie, aber jeder der dran ist hat die Wahl sich oder höher bei Tyranei oder sich oder niedriger bei Dictatorship
    #    historyThisGovernment = readCsv(argv)
    #    print(historyThisGovernment[-1][0])
    elif historyThisGovernment[-1][0] == systemTypeMaps["numstr"][2]:  # Dictatorship
        value = hierarchy(argv, personenAnzahl)
        print("val: " + str(value))
        print("blub: " + str(argv[:3] + value))
        value = voting2(argv[:3] + value, False, False, int(len(value) / 3))
    elif historyThisGovernment[-1][0] == systemTypeMaps["numstr"][3]:  # Tyranei
        value = hierarchy(argv, personenAnzahl)
        print("val: " + str(value))
        print("blub: " + str(argv[:3] + value))
        value = voting2(argv[:3] + value, False, False, -int(len(value) / 3))

    summ = 0
    for val in value[3:]:
        if val != 0:
            summ += 1
    if summ != 0:
        writeCsv(value)

else:
    print(str(systemTypes) + " ???")
