#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# argv
# 1 ist würfel bis zahl
# 2 ist lin log root etc
# zahl n, bei lin zB Schrittweite
# zahl die definiert werden sein soll z.B. 5 Augen als kurz vor Maximum
# sys.argv

def lin(x,n,xe):
    return x*n
def log(x,n,xe):
    return log(x) / log(xe)
def root(x,n,xe):
    return pow(x,1/n) * pow(x,1/xe)
def poly(x,n,xe):
    return pow(x,n) / pow(x,xe)
def expo(x,n,xe):
    return pow(n,x)


fkt = { 'lin' : lin,
        'log' : log,
        'root' : root,
        'poly' : poly,
        'exp' : expo }

def main(inp):
    until = inp[1]
    print(str(until))
    for a in range(inp[1]):
        print(str(fkt[inp[2]](a,inp[3],xe)))


if len(sys.argv) > 3:
    main(sys.argv)
