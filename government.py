#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import csv
import math
import os
import pickle
import random
import sys
from copy import copy

import libdice
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

# example
# ./government.py x vote b 0 1 c 1 1 e 2 1; tail -5 x.txt
# ./government.py x democracy b 1 c 3 e 21
# 0. python exe, 1. logfile, 2. befehl, 3. 3-5 und 6-8 = erste beiden tripel: name zahl zahl, name zahl zahl
# name zahl zahl entspricht den Parametern vom dice und zwar person, würfelaugenersatzwert und Gewichtung
# befehle können sein: vote, revolution, staatsformname

# vote: tripel: eigenname, vote für welche nr, gewicht für das eigene voting

# x.txt
# democracy;c;e;b
# staatssystem und 3 Teilnehmer, ggf. als Rangfolge
# danach voten oder next (next bei keine Demokratie-Elemente)
# vote;1;1;1 bedeutet, erster in der staatform oben bekommt einen Wahlpunkt und hinteren beiden auch
# d.h. c e und b bekommen einen wahlpunkt, bei gewichten von wahlfähigkeit ist es mehr
# das ist alles

# next;2;2;2
# vote;1;2;3

systemTypeMaps = {
    "strint": {
        "democracy": 0,
        "plutocracy": 1,
        "dictatorship": 2,
        "tyrannis": 3,
        "aristocracy": 4,
        "oligarchy": 5,
    },
    "intstr": {
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
systemTypes = systemTypeMaps["intstr"].values()

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


def AristrokratenAmount(argv):
    return math.floor(
        math.sqrt(len(argv[3:]) / 3 + 2)
    )  # ein oberer Bruchteil ist Aristrokrat


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


whoHasMax = set()


def peopleAlreadyDemocraticOrRandomlySelectedInPast(ObjDice=None):
    global whoHasMax
    print("peopleAlreadyDemocraticOrRandomlySelectedInPast")
    print("CSV: " + str(readCsv(argv)))
    thisGovSystemAndVotes = readCsv(argv)
    print("BLUB " + str(thisGovSystemAndVotes))
    allVotes = thisGovSystemAndVotes[:-1]
    govSystem = thisGovSystemAndVotes[-1]
    LastLenOfwhoHasMax = 0
    whoHadMax = copy(whoHasMax)
    whoHasMaxPerTurn: set
    zeroVoters: int
    LastWhoHasMaxPerTurn: int = 0
    LastZeroVoters: int = 0
    deltaMaxVoters: int = None
    deltaZeroVoters: int = None
    electedSummed: set = set()
    electedSummedBefore: set = set()
    elected4aTimespan: set = set()
    elected4aTimespanBefore: set = set()

    for e, csvLine in enumerate(allVotes):
        """letzte zeile aus log txt
        die nummer des letzten wird bei whoHasMax angefügt, bei next
        und bei vote ist es die nummer mit der höchsten zahl
        das ist alles, außer dass dice das auch bekommt, bei next nur
        """
        whoHasMaxPerTurn = set()

        """ Abschnitt A """
        maxVotersPotential = 0
        # print(csvLine)
        for oneCandidateVoteAmount in (
            csvLine[1:]
            if len(whoHasMax) < len(csvLine[1:])
            or len(thisGovSystemAndVotes) > len(csvLine)
            else thisGovSystemAndVotes[1][1:]
            if len(thisGovSystemAndVotes) > 1
            else None
        ):
            if maxVotersPotential < int(oneCandidateVoteAmount):
                maxVotersPotential = int(oneCandidateVoteAmount)
        """ Ende Abschnitt A: Abschnitt A: Bestimmung maxVotersPotential
        Abschnitt B"""

        for i, oneCandidateVoteAmount in enumerate(csvLine[1:]):
            if int(maxVotersPotential) == int(oneCandidateVoteAmount):
                whoHasMax |= {i}
                whoHasMaxPerTurn |= {i}

        """ Ende Abschnitt B: whoHasMax= set of userIDs der obersten """

        # "voteNoRevolution", "voteRevolutionPossible"]:
        """Die User, die nur für die Votes infrage kommen"""
        relevantUsersForSystemsAmount = GetSortOfRelevantUserAmount(
            systemTypeMaps["strint"][historyThisGovernment[-1][0]]
        )

        # print("TCRTECVDFG: " + str(thisGovSystemAndVotes[:-1][-1][1:]))
        """ die User, die Null Votingpower haben """
        zeroVoters = 0
        # for voterAmount in thisGovSystemAndVotes[:-1][-1][1:]:
        for voterAmount in csvLine[1:]:
            if int(voterAmount) == 0:
                zeroVoters += 1

        """ wenn alle bereits gevotet haben, dann Schleifenende """
        """
        LenOfwhoHasMax = len(whoHasMax)
        if (
            LenOfwhoHasMax == LastLenOfwhoHasMax
            or len(whoHasMax) + zeroVoters == relevantUsersForSystemsAmount
        ):
            whoHasMax = whoHadMax
            break
        """
        """invariante muss immer 0 sein """

        invariante = relevantUsersForSystemsAmount - len(whoHasMaxPerTurn) - zeroVoters
        elseNoneZeroNoneMaxVotersAmount = invariante
        """ e > 0, weil Deltas nicht gleich beim ersten Wert berechnet werden können
        """
        if e > 0:
            SetDeltaMaxVoters = LastWhoHasMaxPerTurn - whoHasMaxPerTurn
            IntDeltaZeroVoters = LastZeroVoters - zeroVoters
            deltaInBetweenVotersAmount = (
                LastelseNoneZeroNoneMaxVotersAmount - elseNoneZeroNoneMaxVotersAmount
            )

        electedVotersLastTurn = set([govSystem[who + 1] for who in whoHasMaxPerTurn])
        electedSummed |= electedVotersLastTurn
        elected4aTimespan |= electedVotersLastTurn
        """Wenn die selben Voter wie beim vorherigen (unabhängig von wie Betrag, wie sehr):
        dann nur noch die übrigen erlaubt"""
        if (
            elected4aTimespan == elected4aTimespanBefore
            and csvLine[0] == "voteNoRevolution"
        ):
            """Wenn die Max-Voter-Anzahl erreicht ist, d.h. alle waren mal dran,
            dann können alle noch mal beginnen"""
            if len(elected4aTimespan) == len(govSystem[1:]):
                print("__ Voters geleert")
                elected4aTimespan = copy(whoHasMaxPerTurn)
            else:
                """ ansonsten sind alle dran, die noch nicht dran waren für diesen Abschnitt """
                print("__ übrige Voters dran")
                elected4aTimespan -= set(govSystem[1:])
            whoHasMax = elected4aTimespan

        """ alte aus neuen für Delta-Berechnungen """
        electedSummedBefore = copy(electedSummed)
        elected4aTimespanBefore = copy(elected4aTimespan)
        LastWhoHasMaxPerTurn = copy(whoHasMaxPerTurn)
        LastelseNoneZeroNoneMaxVotersAmount = copy(elseNoneZeroNoneMaxVotersAmount)
        LastZeroVoters = zeroVoters

        print(
            "DiffDeltaVotings "
            + str(e)
            + ": "
            + str(len(whoHasMaxPerTurn))
            + " maxVoters + "
            + " (mit Potential "
            + str(maxVotersPotential)
            + ") "
            + str(zeroVoters)
            + " ZeroVoters of:"
            + str(relevantUsersForSystemsAmount)
            + "delta1u2: "
            + str(deltaMaxVoters)
            + "|"
            + str(deltaZeroVoters)
            + ", elected: "
            + str(electedVotersLastTurn)
            + ", summed up: "
            + str(electedSummed)
            + ", csvLine: "
            + str(csvLine)
        )

        LastLenOfwhoHasMax = len(whoHasMax)
        whoHadMax = copy(whoHasMax)
    """
    print("YY")
    print(str((whoHasMax)))
    print(str(len(whoHasMax)))
    print(str(zeroVoters))
    print(str(relevantUsersForSystemsAmount))
    print("YY")"""
    """ wenn letzter vote eines typs war, dass dabei keine
    Revolutionen stattfinden können und wenn das der letzte Vote in
    allen Abfolgen war, dann gibt es keine Sieger, d.h. keine whoHasMax"""
    if (
        thisGovSystemAndVotes[:-1][-1][0] == "voteNoRevolution"
        and len(whoHasMax) + zeroVoters == relevantUsersForSystemsAmount
    ):
        whoHasMax = set()
        print("whoHasMax now = empty")

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


def newSystem(personenAnzahl, argv, oldsystem=systemTypeMaps["intstr"][3]):
    """
    Bei einem neuen System wird immer der schwächste zum größten und der größte zum kleinsten
    durch die Funktion twistGewichtung
    """
    # print('dd '+str(argv))
    newargv = twistGewichtung(argv)
    # print('ww'+str(newargv))
    if systemTypeMaps["strint"][oldsystem] % 2 == 1:
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


def GetSortOfRelevantUserAmount(govType: int) -> int:
    global argv
    govType = int(govType)
    print("GOV: " + str(govType))
    print("GOV: " + str(systemTypeMaps["strint"]["oligarchy"]))
    print("GOV: " + str(AristrokratenAmount(argv)))
    print("GOV: " + str(systemTypeMaps["strint"]))
    return (
        int(len(argv[3:]) / 3)
        if govType
        in (
            systemTypeMaps["strint"]["democracy"],
            systemTypeMaps["strint"]["plutocracy"],
            systemTypeMaps["strint"]["dictatorship"],
        )
        else AristrokratenAmount(argv)
        if govType
        in (
            systemTypeMaps["strint"]["aristocracy"],
            systemTypeMaps["strint"]["oligarchy"],
        )
        else 1
        if govType in (systemTypeMaps["strint"]["tyrannis"],)
        else None
    )


def voting(
    userAmount,
    votes,
    potentials,
    govType=0,
    voteHierarchy=0,
):
    global whoHasMax
    # aristokratenAmount = AristrokratenAmount(argv)
    print("XX")
    print(str(votes))
    print(str(potentials))
    print(str(whoHasMax))
    print("XX")
    results = {}
    """ Revolution, wenn alle durch sind und dann alle votes=0 returnen, ende"""

    sortOfRelevantUserAmount = GetSortOfRelevantUserAmount(govType)

    if (
        userAmount == len(whoHasMax) or len(readCsv(argv)) > sortOfRelevantUserAmount
    ) and argv[2] in ["voteOnce"]:
        print("Alle restlichen User sind dran, dann neues System!")
        revolution(argv)
        for num in range(userAmount):
            results[num] = 0
        return results

    """ zunächst sind alle votes 0"""
    for i in range(userAmount):
        results[i] = 0
    """
    + bei weniger als alle aristrokaten, stopp, so dass dann nur die aristrokraten wählen
    + for votes for user, d.h. jeder user votet jeden user, es sei denn Aristrokratie
    + """

    for k, (vote, potential) in enumerate(zip(votes, potentials)):

        # if (
        # (
        # (
        # govType
        # in (
        # systemTypeMaps["strint"]["aristocracy"],
        # systemTypeMaps["strint"]["oligarchy"],
        # )
        # and aristokratenAmount <= k
        # )
        # )
        # or govType == systemTypeMaps["strint"]["tyrannis"]
        # and k == 1
        # ):
        # print(
        # "arist or olig: voting stopped for not all to vote "
        # + str(k)
        # + " of "
        # + str(len(votes))
        # )
        # break
        for i in range(userAmount)[:sortOfRelevantUserAmount]:
            # print("user: " + str(i))
            if int(i) == int(vote):
                # print("vote: " + str(vote))
                """voteHierarchy definiert sich daraus welche user voten dürfen - das ist alles
                + der max user fällt immer weg, der user mit der nummer whoHasMax
                + in Oligarchie haben user dreifaches potential
                    aber int(boolwert) * 3 ist irgendwie komisch aber funktionierend programmiert
                + wo kommt eigentlich potentials her?: Das sind die gewichte, letzter wert im tripel
                + if true oder false, immer: resultliste hat immer den wert 1 * potentialvariable
                """
                if i not in whoHasMax or len(whoHasMax) >= sortOfRelevantUserAmount:
                    if (
                        voteHierarchy
                        == 0
                        # or (voteHierarchy != 0 and voteHierarchy - 1 <= i)
                        # or (voteHierarchy > 0 and voteHierarchy - 1 <= i)
                        # or (voteHierarchy < 0 and -voteHierarchy - 1 >= i)
                    ):
                        # if oligarchy and i == k:
                        #    potential = int(oligarchy) * 3
                        # if not i in results.keys():
                        # results[i] = 1 * int(potential)
                        # else:
                        # results[i] += 1 * int(potential)
                        results[i] += (
                            int(potential)
                            if govType
                            in (
                                systemTypeMaps["strint"]["oligarchy"],
                                systemTypeMaps["strint"]["tyrannis"],
                                systemTypeMaps["strint"]["plutocracy"],
                            )
                            else (
                                len(votes) - 1
                                if (len(votes) - 2) > 0
                                else len(votes)
                                if (len(votes) - 1) > 0
                                else 1
                            )
                            if govType == systemTypeMaps["strint"]["dictatorship"]
                            and k == 0
                            else 1
                        )
                # elif govType == systemTypeMaps["strint"]["dictatorship"]:
                #    results[i] = 20

    print("results " + str(results))
    """ revolution nach vote, wenn es letzter vote war
    + immer returnen der Potentialliste per i = user"""
    isNotZero = 0
    for result in results.values():
        if int(result) != 0:
            isNotZero += 1
    if isNotZero == 0 and argv[2] in ["voteOnce"]:
        print("revol am Ende von votes")
        revolution(argv)
    return results


def voting2(
    argv,
    govType,
):
    """tripel in liste, dann vote()
    dann dessen ergebnis returned, einzelne, keine tripel
    aber davor noch die 3 ersten parameter, wozu wohl auch die py datei gehört
    das als liste returned
    """

    """ unten Hat momentan keine Funktion """
    print("BLUB: " + str(govType))
    print("BLUB: " + str(systemTypeMaps["strint"]["dictatorship"]))
    if govType in (
        systemTypeMaps["strint"]["tyrannis"],
        systemTypeMaps["strint"]["dictatorship"],
    ):
        triplesList_NotTripleInList = hierarchy(argv, personenAnzahl)
        print("ED: " + str(triplesList_NotTripleInList))
        triplesList_NotTripleInList = argv[3:]
        print("EF: " + str(triplesList_NotTripleInList))
        argv = argv[:3] + triplesList_NotTripleInList
        voteHierarchy = int(len(triplesList_NotTripleInList) / 3)
        print("BLA: " + str(voteHierarchy))
    else:
        voteHierarchy = 0
    """ oben Hat momentan keine Funktion """

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
    # print("VOTESbefore: " + str(votes))
    # votingResults = voting(len(names), votes, potentials, govType, voteHierarchy)
    votingResults = voting(len(names), votes, potentials, govType)
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
    """
    # von Demokratie auf Plutokratie
    # von x modulo 2 = 0 auf darauf folgendes x += 1
    # d.h. von einem der guten 3 auf das böse immer
    # von modulo 2 = 1 auf irgendein anderes x modulo 2 = 0
    # aber nicht das, was das entsprechende x modulo 2 = 0 wäre das davor liegen
    # d.h. von etwas bösem auf ein anderes gutes, aber nicht dessen gutes, sondern etwas neues
    # würde"""
    oldsystem = readCsv(argv)[-1][0]
    print("oldsystem: " + str(systemTypeMaps["strint"][oldsystem]))
    if systemTypeMaps["strint"][oldsystem] % 2 == 0:
        print("mod == 0")
        newsystem = systemTypeMaps["intstr"][
            (systemTypeMaps["strint"][oldsystem] + 1) % 6
        ]
    else:
        print("mod == 1")
        randbool = random.randint(0, 1)  # randint 0 1 macht 0 oder 1 möglich
        newsystem = systemTypeMaps["intstr"][
            (systemTypeMaps["strint"][oldsystem] + 1 + (2 * randbool)) % 6
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
elif argv[2] in ["voteOnce", "voteNoRevolution", "voteRevolutionPossible"]:
    """ alle Staatsformen durchprobieren, wenn vote als Befehl verwendet wurde """
    historyThisGovernment = readCsv(argv)
    """ UMSORTIERUNG DER ARGV"""
    argv = argv[:3] + orderOfPrecedence(argv, historyThisGovernment[-1][1:])
    print("umsortierete Voter: " + str(argv))
    """ Welche User haben zusammen das Maximalgewicht """
    whoHasMax = peopleAlreadyDemocraticOrRandomlySelectedInPast()
    print("whoHasMax: " + str(whoHasMax))

    if namesNotAllDifferent:
        print("Some names are equal. Exit!")
        exit()
    # for whoNotAnymore in whoHasMax:
    #    print(argv[whoNotAnymore*3+4])
    #    argv[whoNotAnymore*3+4] = -abs(int(argv[whoNotAnymore*3+4]))
    # print(argv)
    # print(historyThisGovernment[-1][0])
    """ alle Staatsformen durchprobieren, wenn vote als Befehl verwendet wurde """
    if (
        historyThisGovernment[-1][0] == systemTypeMaps["strstr"]["democracy"]
    ):  # Demokratie
        # value = voting2(argv)
        print("Demokratie")
        value = voting2(argv, 0)
    elif (
        historyThisGovernment[-1][0] == systemTypeMaps["strstr"]["aristocracy"]
    ):  # Aristrokratie
        print("vote in Aristokratie")
        # longvar = ("dice.py "+str(personenAnzahl)+" gewicht lin 1 1 1 lin 1 1 1").split()
        # hierarchyGame = libdice.dice(longvar, werfen=0, uniq_=True, bezeichner=' '.join(argv[4:]))
        # print('out: '+str(hierarchyGame.out()))
        """ Unterschied zur Demokratie, dadurch dass die meisten nicht wählen können """
        # value = voting2(argv, True)
        value = voting2(argv, 4)
    elif (
        historyThisGovernment[-1][0] == systemTypeMaps["strstr"]["plutocracy"]
    ):  # Plutokratie
        """ kein Unterschied zur Demokratie, trotz dieser 2 bool Werte !  """
        # value = voting2(argv, False, True)
        value = voting2(argv, 1)
    elif (
        historyThisGovernment[-1][0]
        == systemTypeMaps["strstr"]["oligarchy"]  # oligarchy
    ):  # Oligarchie - Programmiere ich später - mehr Eigennutz der Chefs, d.h. normale Wahl und dürfen bei jedem zweiten Mal selbst
        # def voting2(argv, aristrokratsAreLessThanAll=False,Plutocracy=False,voteHierarchy=0,oligarchy=False):
        """ erster boolwert = nur wenige wählen wie bei aristrokratie, Zweiter Boolwert nie eine Auswirkung,  """
        # value = voting2(argv, True, True, 0, True)
        value = voting2(argv, 5)
    #    if value[2] == 'vote':
    #       writeCsv(value)
    #
    # elif argv[2] in ['next']:  # Tyranei und Dictatorship: beides Hierarchie, aber jeder der dran ist hat die Wahl sich oder höher bei Tyranei oder sich oder niedriger bei Dictatorship
    #    historyThisGovernment = readCsv(argv)
    #    print(historyThisGovernment[-1][0])

    elif (
        historyThisGovernment[-1][0] == systemTypeMaps["strstr"]["dictatorship"]
    ):  # Dictatorship
        # value = hierarchy(argv, personenAnzahl)
        # print("val: " + str(value))
        # print("blub: " + str(argv[:3] + value))
        # value = voting2(
        #    argv[:3] + value, False, False, int(len(value) / 3), False, False
        # )
        value = voting2(argv, 2)
    elif (
        historyThisGovernment[-1][0] == systemTypeMaps["strstr"]["tyrannis"]
    ):  # Tyranei
        # value = hierarchy(argv, personenAnzahl)
        # print("val: " + str(value))
        # print("blub: " + str(argv[:3] + value))
        # value = voting2(
        #    argv[:3] + value, False, False, -int(len(value) / 3), False, True
        # )
        value = voting2(argv, 3)

    summ = 0
    print("LastValues: " + str(value[3:]))
    for val in value[3:]:
        if val != 0:
            summ += 1
    if summ != 0:
        writeCsv(value)
    else:
        print("NOT WRITE TO CSV: " + str(value[3:]))

else:
    print(str(systemTypes) + " ???")
