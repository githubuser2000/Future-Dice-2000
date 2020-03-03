#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import libdice
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

def help_():
    print("dice.py 3 -lin 3 2 7")
    print("dice.py 3 gewicht poly 3 2 0.7 -poly 1 2 5")
    print("dice.py 3 gewicht lin 3 3 7 lin 3 3 7")
    print("dice.py 3 kombi 3 3 0.7")
    print("dice.py 3 rand 3 3 5")

if len(sys.argv) > 5:
    app =QApplication(sys.argv)
    libdice.dice.languages(app,QQmlApplicationEngine())
    dice = libdice.dice(sys.argv)
    dice.rootContext().setContextProperty("dice", dice)
    #sys.exit(app.exec_())
    dice.out()
else:
    help_()
