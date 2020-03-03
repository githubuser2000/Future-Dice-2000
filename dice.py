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
    libdice.dice.languages1(app)
    qAppEngin = QQmlApplicationEngine()
    libdice_strlist = [qAppEngin.tr('lin'), qAppEngin.tr('log'), qAppEngin.tr('root'), qAppEngin.tr('poly'), qAppEngin.tr('exp'), qAppEngin.tr('kombi'), qAppEngin.tr('logistic'), qAppEngin.tr('rand'), qAppEngin.tr('gewicht'), qAppEngin.tr('add'), qAppEngin.tr('mul'), qAppEngin.tr("Wuerfelwurf: "),qAppEngin.tr(" (Wuerfelaugen ")]
    blub = [qAppEngin.tr('test')]
    libdice.dice.languages2(libdice_strlist)
    print(str(blub[0]))
    print(blub)
    dice = libdice.dice(sys.argv)
    #sys.exit(app.exec_())
    dice.out()
else:
    help_()
