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

randfkt = { 1 : lin,
        2 : log,
        3 : root,
        4 : poly,
        5 : expo }

randfktvar2 = { 1 : 'lin',
        2 : 'log',
        3 : 'root',
        4 : 'poly',
        5 : 'exp' }

randfktvar = random.randrange(5)+1

def rand(x,n,xe,e):
    print(str(randfktvar))
    print(str(randfktvar2[randfktvar]))
    return randfkt[randfktvar](x,n,xe,e)

fkt = { 'lin' : lin,
        'log' : log,
        'root' : root,
        'poly' : poly,
        'exp' : expo,
        'rand' : rand}

def main(inp):
    until = inp[1]
    inp[4] = int(inp[4])
    inp[5] = float(inp[5])
    inp[1] = int(inp[1])
    if inp[4] <= inp[1] and inp[4] > 1 and ( inp[2] != 'rand' or inp[1] < 6):# and inp[5] <= inp[1] and inp[5] > 1:
        #inp[4]-=1
        #inp[5]-=1
        for a in range(1,int(inp[1])+1):
            print(str(fkt[inp[2]](int(a),int(inp[3]),int(inp[4]),inp[5])))


if len(sys.argv) > 5:
    main(sys.argv)
