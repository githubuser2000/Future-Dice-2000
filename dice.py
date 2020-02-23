#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math
import random
#from collections import defaultdict
# argv
# 1 ist würfel bis zahl
# 2 ist lin log root etc
# zahl n, bei lin zB Schrittweite
# zahl die definiert werden sein soll z.B. 5 Augen als kurz vor Maximum
# sys.argv

inpp_ = None
include1 = None
include2 = None
include3 = None

def sigmoid(x,n,xe,e,xth=0):
    x-=int(inpp_[1])/2
    xe-=int(inpp_[1])/2
    return ( n / (n + math.exp(-x)) ) / ( n / (n + math.exp(-xe)) ) * e

def lin(x,n,xe,e,xth=0):
    #print(str(x))
    #print(str(e))
    #print(str(xe))
    return (x * e) / xe
def log(x,n,xe,e,xth=0):
    return math.log(x,n) / math.log(xe,n) * e
def root(x,n,xe,e,xth=0):
    return pow(x,1/n) / pow(xe,1/n) * e
def poly(x,n,xe,e,xth=0):
    return pow(x,n) / pow(xe,n) * e
def expo(x,n,xe,e,xth=0):
    return pow(n,x) / pow(n,xe) * e

def randselect(includex):
        d = 1000
        randfktvarx = random.randrange(len(includex))+1
        while not includex[randfktvarx-1]:
            d-=1
            if d <= 0:
                return None
            randfktvarx = random.randrange(len(includex))+1
        return randfktvarx

def kombi(x,n,xe,e,reku = 50,xth=0):
    global include1,include2,include3
    try:
    #if True:
        okay1 = False
        okay2 = False
        for i,k in zip(include1,include2):
            if i:
                okay1 = True
            if k:
                okay2 = True

        if not okay1 or not okay2:
            return None
        randfktvar1,randfktvar2,randfktvar3 = randselect(include1),randselect(include2),randselect(include3)
        #print("-- "+str(randfktvar1)+" "+str(randfktvar2)+" "+str(randfktvar3))

        if randfktvar3 == 1:
            print("Kombi Mulitply: "+str(randfkt2[randfktvar1])+" "+str(randfkt2[randfktvar2]))
            return randfkt[randfktvar1](x,n,xe,e) * randfkt[randfktvar2](x,n,xe,e)
        elif randfktvar3 == 2:
            print("Kombi Addition "+str(randfkt2[randfktvar1])+" "+str(randfkt2[randfktvar2]))
            return randfkt[randfktvar1](x,n,xe,e) + randfkt[randfktvar2](x,n,xe,e)
        elif randfktvar3 == 3:
            print("Kombi Logarithm "+str(randfkt2[randfktvar1])+" "+str(randfkt2[randfktvar2]))
            return math.log(randfkt[randfktvar1](x,n,xe,e)+1.1,randfkt[randfktvar2](x,n,xe,e)+1.1)
        elif randfktvar3 == 4:
            print("Kombi Root "+str(randfkt2[randfktvar1])+" "+str(randfkt2[randfktvar2]))
            return pow(randfkt[randfktvar1](x,n,xe,e), 1 / ( randfkt[randfktvar2](x,n,xe,e) + 1 ))
    except:
        if reku > 0:
            reku -= 1
            return kombi(x,n,xe,e,reku)

def gewicht(type1,x,n,xe,e,type2,n2,xe2,e2):
    return ( fkt[type1](x,n,xe,e),
            fkt[type2](x,n2,xe2,e2,1) )


def rand(x,n,xe,e,xth=0):
    global include1,include2, randfktvarA
    okay1 = False
    for i in include1:
        if i:
            okay1 = True
    if not okay1:
        return 1
    randfktvarA = randselect(include1 if xth == 0 else include2)
    result = randfkt[randfktvarA](x,n,xe,e)
    return result


fkt = { 'lin' : lin,
        'log' : log,
        'root' : root,
        'poly' : poly,
        'exp' : expo,
        'rand' : rand,
        'kombi' : kombi,
        'gewicht' : gewicht,
        '-lin' : lin,
        '-log' : log,
        '-root' : root,
        '-poly' : poly,
        '-exp' : expo,
        '-rand' : rand,
        '-kombi' : kombi,
        'logistic' : sigmoid,
        '-logistic' : sigmoid}



randfkt = { 1 : lin,
        2 : log,
        3 : root,
        4 : poly,
        5 : expo,
        6 : kombi,
        7 : sigmoid,
        8 : rand,
        9 : gewicht}

randfkt2 = { 1 : 'lin',
        2 : 'log',
        3 : 'root',
        4 : 'poly',
        5 : 'exp',
        6 : 'kombi',
        7 : 'logistic',
        8 : 'rand',
        9 : 'gewicht'}

randfkt3 = { 1 : 'mul',
        2 : 'add',
        3 : 'log',
        4 : 'root'}


def weightedrand(weights):
    summ = 0
    sum2 = []
    for weight in weights:
        summ += weight
        sum2.append(summ)

    rand1 = random.random() * summ

    for i,asum in enumerate(sum2):
        if rand1 < asum:
            return i # +1

    return None



def help():
    print("dice.py 3 -lin 3 2 7")
    print("dice.py 3 gewicht poly 3 2 0.7 -poly 1 2 5")
    print("dice.py 3 gewicht lin 3 3 7 lin 3 3 7")
    print("dice.py 3 kombi 3 3 0.7")
    print("dice.py 3 rand 3 3 5")

wuerfeltype = None
wuerfelAugenSet = set()
values, wuerfelType, wuerfelWuerfe, uniq, randos = None, None, None, None, None


def wuerfeln():
    global wuerfelAugenSet
    global values, wuerfelType, wuerfelWuerfe, uniq, randos
    wuerfelWuerfe2 = []
    if len(wuerfelAugenSet) == len(values):
        wuerfelAugenSet = set()
    if wuerfelType == 0:
        while True:
            dice = random.randrange(len(values))
            if not dice in wuerfelAugenSet or not uniq:
                wuerfelAugenSet.add(dice)
                break
        wuerfelWuerfe2.append((dice,values[dice]))
        wuerfelWuerfe.append((dice,values[dice]))
        print("Würfelwurf: "+str(values[dice])+" (Würfelaugen "+str(dice+1)+")")
    elif wuerfelType == 1:
        while True:
            dice = weightedrand(randos)
            if not dice in wuerfelAugenSet or not uniq:
                wuerfelAugenSet.add(dice)
                break
        print("rand augenzahl ergebnis: "+str(dice))
        #dice = random.randrange(inp[1])+1
        ergebnis = (randos[dice],values[dice])
        wuerfelWuerfe2.append((dice,ergebnis[0],ergebnis[1]))
        wuerfelWuerfe.append((dice,ergebnis[0],ergebnis[1]))
        print("Würfelwurf: "+str(values[dice])+" (Würfelaugen "+str(dice)+")")
    return wuerfelWuerfe2

def main(inp,werfen = 2, uniq_ = False):
    global randfktvarA, inpp_
    global include1,include2,include3
    global values, wuerfelType, wuerfelWuerfe, uniq, randos
    inpp_ = inp
    wuerfelWuerfe = werfen
    uniq = uniq_
    wuerfelWuerfe = []
    wuerfelWuerfeMoeglichkeiten = {}
    if len(inp) > 3:
        if type(inp[-3]) is list and type(inp[-2]) is list and type(inp[-1]) is list:
            include1,include2,include3 = inp[-3],inp[-2],inp[-1]
            print('_'+str(include1))
            inp=inp[:-3]
        else:
            i1,i2,i3 = [],[],[True,True,True,True]
            for i in range(len(randfkt2)):
                i1.append(True)
                i2.append(True)
            include1,include2,include3 = i1,i2,i3
    if len(inp) == 6:
        until = int(inp[1])
        inp[4] = int(inp[4])
        inp[5] = float(inp[5])
        inp[3] = float(inp[3])
        inp[1] = int(inp[1])
        if inp[4] <= inp[1] and inp[4] > 1 and inp[2] != "gewicht":
            values = []
            for a in range(1,until+1):
                values.append(fkt[inp[2]](a,inp[3],inp[4],inp[5]))
            if inp[2][0]=='-':
                values.reverse()
            for i,value in enumerate(values):
                wuerfelWuerfeMoeglichkeiten[i] = value
                print(str(i+1)+": "+str(value))
            for i in range(werfen):
                wuerfelType = 0
                wuerfelWuerfe.append(wuerfeln())
    elif len(inp) == 11 and inp[2] == "gewicht":
        print("d")
        until = int(inp[1])
        inp[4] = int(inp[4])
        inp[5] = int(inp[5])
        inp[6] = float(inp[6])
        inp[1] = int(inp[1])
        inp[8] = float(inp[8])
        inp[9] = int(inp[9])
        inp[10] = float(inp[10])
        if inp[5] <= inp[1] and inp[5] > 0 and inp[9] <= inp[1] and inp[9] > 0:
            randos = []
            values = []
            for a in range(1,until+1):
                thing = fkt['gewicht'](inp[3],a,inp[4],inp[5],inp[6],inp[7],inp[8],inp[9],inp[10])
                randos.append(thing[0])
                values.append(thing[1])
            if inp[3][0]=='-':
                randos.reverse()
            if inp[7][0]=='-':
                values.reverse()
            for i,(rando,value) in enumerate(zip(randos,values)):
                wuerfelWuerfeMoeglichkeiten[i] = (rando,value)
                print(str(i+1)+": "+str(value))
                print(str(i+1)+": "+str(rando)+", "+str(value))
            for i in range(werfen):
                wuerfelType = 1
                wuerfelWuerfe.append(wuerfeln())
    else:
        help()
        return None
    result = (wuerfelWuerfeMoeglichkeiten,wuerfelWuerfe)
    print(str(result))
    return result


if len(sys.argv) > 5:
    main(sys.argv)
else:
    help()
