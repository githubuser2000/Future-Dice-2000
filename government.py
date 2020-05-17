#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import libdice
import sys
import csv
import os

def writeCsv(data):
    with open(data[1]+'.txt', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(data[2:])

def readCsv(data):
    with open(data[1]+'.txt', mode='r') as csv_file:
        for row in reversed(list(csv.reader(csv_file))):
            print ('; '.join(row))

systemTypes = ['democrazy','dictatorship','aristocracy']


if sys.argv[2] in systemTypes:
    writeCsv(sys.argv)
else:
    print(str(systemTypes)+" ???")

readCsv(sys.argv)


