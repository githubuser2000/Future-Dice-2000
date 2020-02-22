#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent, QQmlContext
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore
from PyQt5.QtQuick import QQuickView, QQuickItem
from PyQt5.QtCore import QObject
#from UM.Application import Application

class blub(QObject):
    pass

def runQML():
    #view = QQuickView()
    #ui.setupUi(this)
    #container = QWidget.createWindowContainer(view, this)
    #container.setMinimumSize(200, 200)
    #container.setMaximumSize(200, 200)
    app =QApplication(sys.argv)
    engine = QQmlApplicationEngine()
#    app.setWindowIcon(QIcon("icon.png"))
    root = engine.rootContext()
    engine.load('dice/main.qml')
    component = QQmlComponent(engine, 'dice/Radio1.qml')
    #ui.verticalLayout.addWidget(container)
    child = engine.rootObjects()[0].findChild(QtCore.QObject, "foo_object")
    #print(str(child))
    child.setProperty("text", "Blödsinn")
    #root.setContextProperty("guisettings", guisettings)



    #print(str(len(engine.rootObjects())))
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    for w in engine.rootObjects():
        #print(str(w))
        #print(str(type(w.contentItem().childItems()).__name__))
        for v in w.contentItem().childItems():
            #print(str(v.setOpacity(0.9)))
            for i,x in enumerate(v.childItems()):
                #print(str(x.setOpacity(0.9)))
                ##x.stackAfter(v.childItems()[0])
                #print(str(v.childItems()[0]))
                pass
    #engine.rootObjects()[0].contentItem().childItems()[0].childItems()[0].stackAfter(QQuickView())
    component.create()
    #print(str(component))
    context = QQmlContext(engine.rootContext())
    context.setContextProperty("liste", blub)
    view = component.create(context)
    #print(str(view))
    engine.rootObjects()[0].contentItem().childItems()[0].childItems()[1]=view
    for a in engine.rootObjects()[0].contentItem().childItems()[0].childItems()
        a = view
    #for w in engine.rootObjects():
    #    pass




    if not engine.rootObjects():
        return -1

    return app.exec_()




if __name__ == "__main__":
    sys.exit(runQML())
