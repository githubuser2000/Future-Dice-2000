#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent, QQmlContext
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore
from PyQt5.QtQuick import QQuickView, QQuickItem
from PyQt5.QtCore import QObject, QAbstractListModel, QModelIndex, Qt, QVariant
import dice

class analysistypes():
    def __init__(self,name):
        self.nam = name
    def name(self):
        return self.nam
    def checked(self):
        if self.name == 'lin':
            return True
        else:
            return False
class Model(QAbstractListModel):

    #WidthRole = Qt.UserRole + 1
    #HeightRole = Qt.UserRole + 2
    #ColorRole = Qt.UserRole + 3
#
    #_roles = {WidthRole: b"width", HeightRole: b"height", ColorRole: b"color"}
    NameRole = Qt.UserRole + 1
    CheckedRole = Qt.UserRole + 2

    _roles = {NameRole: b"name", CheckedRole: b"checked"}
    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)

        self._datas = []

    def addData(self, data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._datas.append(data)
        self.endInsertRows()

    def rowCount(self, parent=QModelIndex()):
        return len(self._datas)

    def data(self, index, role=Qt.DisplayRole):
        try:
            data = self._datas[index.row()]
        except IndexError:
            return QVariant()
        if role == self.NameRole:
            return data.name()
        if role == self.CheckedRole:
            return data.checked()

        return QVariant()

    def roleNames(self):
        return self._roles
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
    radios = engine.rootObjects()[0].findChild(QtCore.QObject, "radios")
    #print(str(child))
    child.setProperty("text", "Blödsinn")
    print(str(dice.randfkt2.values()))
    #radios.setProperty("model", list(dice.randfkt2.values()))
    radiomodel = Model()
    for el in dice.randfkt2.values():
        radiomodel.addData(analysistypes(el))
        print(radiomodel.data(0,CheckedRole))
    radios.setProperty("radiomodel", radiomodel )
    #lin = radios.children()[1]
    #print(str(lin))
    #print(str(lin.property("checked")))
    #lin.setProperty("checked", 1 )
    #root.setContextProperty("guisettings", guisettings)



    #print(str(len(engine.rootObjects())))
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    for w in engine.rootObjects():
        #print(str(w))
        #print(str(type(w.contentItem().childItems()).__name__))
        for v in w.contentItem().childItems():
            print(str(v))
            for i,x in enumerate(v.childItems()):
                #print(str(x.setOpacity(0.9)))
                ##x.stackAfter(v.childItems()[0])
                #print(str(v.childItems()[0]))
                pass
    #engine.rootObjects()[0].contentItem().childItems()[0].childItems()[0].stackAfter(QQuickView())
    component.create()
    #print(str(component))
    context = QQmlContext(engine.rootContext())
    #context.setContextProperty("liste", blub)
    view = component.create(context)
    #print(str(view))
    engine.rootObjects()[0].contentItem().childItems()[0].childItems()[1]=view
    for a in engine.rootObjects()[0].contentItem().childItems()[0].childItems():
        a = view
    #for w in engine.rootObjects():
    #    pass




    if not engine.rootObjects():
        return -1

    return app.exec_()




if __name__ == "__main__":
    sys.exit(runQML())
