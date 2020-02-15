#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math
import random

# argv
# 1 ist würfel bis zahl
# 2 ist lin log root etc
# zahl n, bei lin zB Schrittweite
# zahl die definiert werden sein soll z.B. 5 Augen als kurz vor Maximum
# sys.argv

def lin(x,n,xe,e):
    #print(str(x))
    #print(str(e))
    #print(str(xe))
    return (x * e) / xe
def log(x,n,xe,e):
    return math.log(x,n) / math.log(xe,n) * e
def root(x,n,xe,e):
    return pow(x,1/n) / pow(xe,1/n) * e
def poly(x,n,xe,e):
    return pow(x,n) / pow(xe,n) * e
def expo(x,n,xe,e):
    return pow(n,x) / pow(n,xe) * e

def kombi(x,n,xe,e):
    randfktvar = random.randrange(6)+1
    randfktvar2 = random.randrange(6)+1
    randfktvar3 = random.randrange(4)+1
    if randfktvar3 == 1:
        print("Kombi Mulitply: "+str(randfkt2[randfktvar])+" "+str(randfkt2[randfktvar2]))
        return randfkt[randfktvar](x,n,xe,e) * randfkt[randfktvar2](x,n,xe,e)
    elif randfktvar3 == 2:
        print("Kombi Addition "+str(randfkt2[randfktvar])+" "+str(randfkt2[randfktvar2]))
        return randfkt[randfktvar](x,n,xe,e) + randfkt[randfktvar2](x,n,xe,e)
    elif randfktvar3 == 3:
        print("Kombi Logarithm "+str(randfkt2[randfktvar])+" "+str(randfkt2[randfktvar2]))
        return math.log(randfkt[randfktvar](x,n,xe,e)+1.1,randfkt[randfktvar2](x,n,xe,e)+1.1)
    elif randfktvar3 == 4:
        print("Kombi Root "+str(randfkt2[randfktvar])+" "+str(randfkt2[randfktvar2]))
        return pow(randfkt[randfktvar](x,n,xe,e), 1 / ( randfkt[randfktvar2](x,n,xe,e) + 1 ))

randfkt = { 1 : lin,
        2 : log,
        3 : root,
        4 : poly,
        5 : expo,
        6 : kombi }

randfkt2 = { 1 : 'lin',
        2 : 'log',
        3 : 'root',
        4 : 'poly',
        5 : 'exp',
        6 : 'kombi' }

randfktvar = random.randrange(6)+1
randfktvar2 = random.randrange(6)+1


def rand(x,n,xe,e):
    #print(str(randfktvar))
    if x == 1:
        print(str(randfkt2[randfktvar]))
    return randfkt[randfktvar](x,n,xe,e)



fkt = { 'lin' : lin,
        'log' : log,
        'root' : root,
        'poly' : poly,
        'exp' : expo,
        'rand' : rand,
        'kombi' : kombi}

def main(inp):
    until = inp[1]
    inp[4] = int(inp[4])
    inp[5] = float(inp[5])
    inp[1] = int(inp[1])
    if inp[4] <= inp[1] and inp[4] > 1:
        for a in range(1,int(inp[1])+1):
            print(str(a)+": "+str(fkt[inp[2]](int(a),int(inp[3]),int(inp[4]),inp[5])))
        dice = random.randrange(inp[1])+1
        print("Würfelwurf: "+str(fkt[inp[2]](dice,int(inp[3]),int(inp[4]),inp[5]))+" (Würfelaugen "+str(dice)+")")


if len(sys.argv) > 5:
    main(sys.argv)
