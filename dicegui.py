#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore

class guisettings():
    info = 'text'


def runQML():
    app =QApplication(sys.argv)
    engine = QQmlApplicationEngine()
#    app.setWindowIcon(QIcon("icon.png"))
    root = engine.rootContext()
    engine.load('dice/main.qml')
    child = engine.rootObjects()[0].findChild(QtCore.QObject, "foo_object")
    #print(str(child))
    child.setProperty("text", "Blödsinn")
    #root.setContextProperty("guisettings", guisettings)


    if not engine.rootObjects():
        return -1

    return app.exec_()




if __name__ == "__main__":
    sys.exit(runQML())
