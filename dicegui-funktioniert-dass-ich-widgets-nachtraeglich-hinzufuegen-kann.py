#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore
from PyQt5.QtQuick import QQuickView



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
    #ui.verticalLayout.addWidget(container)
    child = engine.rootObjects()[0].findChild(QtCore.QObject, "foo_object")
    #print(str(child))
    child.setProperty("text", "Blödsinn")
    #root.setContextProperty("guisettings", guisettings)



    print(str(len(engine.rootObjects())))
    for w in engine.rootObjects():
        #print(str(type(w.contentItem().childItems()).__name__))
        for v in w.contentItem().childItems():
            print(str(v.setOpacity(0.9)))
            for i,x in enumerate(v.childItems()):
                print(str(x.setOpacity(0.9)))
                x.stackAfter(v.childItems()[-i])




    if not engine.rootObjects():
        return -1

    return app.exec_()




if __name__ == "__main__":
    sys.exit(runQML())
