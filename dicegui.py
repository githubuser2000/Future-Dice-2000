#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent, QQmlContext
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys
#from PyQt5 import QtCore
from PyQt5.QtQuick import QQuickView, QQuickItem
from PyQt5.QtCore import QObject, QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot, QUrl
import dice
import model2

class MainWindow(QQmlApplicationEngine):
    wuerfelrestellt = False
#    radi = 'lin'

    @pyqtSlot()
    def getRadioBselected(self):
        print(str(self.radi))
        #radios = self.rootObjects()[0].findChild(QObject, "radiolayout")
        #print(radios.property["objectName"])
        #for i,radio in enumerate(radios.children()):
        #    print(str(radio.property("text")))
        #    print(str("x"+str(radio.property("checked"))))
        #    if radio.property("checked"):
        #        print(dice.randfkt2[i+1])

    @pyqtSlot()
    def wuerfeln2(self):
        #print(str(self.radios.property("checksate")))
        if not self.wuerfelrestellt:
            self.wuerfelErstellen()
        else:
            wuerfe = self.rootObjects()[0].findChild(QObject, "wuerfe")
            for i in range(int(wuerfe.property("text"))):
                result = dice.wuerfeln()
                print("r " + str(result) )
                for ell in result:
                    for i,el in enumerate(ell):
                        self.scrollmodel.insertPerson(i, str(el), True)
    @pyqtSlot()
    def wuerfelErstellen(self):
        if not self.wuerfelrestellt:
            self.wuerfelrestellt = True
            wuerfe = self.rootObjects()[0].findChild(QObject, "wuerfe")
            n = self.rootObjects()[0].findChild(QObject, "n")
            x = self.rootObjects()[0].findChild(QObject, "x")
            y = self.rootObjects()[0].findChild(QObject, "y")
            augen = self.rootObjects()[0].findChild(QObject, "augen")
            sview = self.rootObjects()[0].findChild(QObject, "scrollView")
            print("x")
            #wuerfe.setProperty("text", "x" )
            LRad = self.rootObjects()[0].findChild(QObject, "LRad")
            #print(str(blub))
            print(str(LRad.property("text")))
            #print(str(self.radiogroup))
            #print(str(self.radiogroup.property("ButtonGroup")))
            #priint(wuerfe.property("text"))

            #print(wuerfe.property("text"))
            result = dice.main(['dicegui',augen.property("text"),LRad.property("text"),n.property("text"),x.property("text"),y.property("text")],int(wuerfe.property("text")), False)
            for ell in result:
                for i,el in enumerate(ell):
                    self.scrollmodel.insertPerson(i, str(el), True)
    def __init__(self):
        super().__init__()
        self.radiomodel = model2.PersonModel()
        self.scrollmodel = model2.PersonModel()
        self.chkmodel1,self.chkmodel2,self.chkmodel3 = model2.PersonModel(),model2.PersonModel(),model2.PersonModel()
        for i,el in enumerate(list(dice.randfkt2.values())):
            self.radiomodel.insertPerson(i, el, True if i==0 else False)
            self.chkmodel1.insertPerson(i, el, True)
            self.chkmodel2.insertPerson(i, el, True)
        for i,el in enumerate(list(dice.randfkt3.values())):
            self.chkmodel3.insertPerson(i, el, True)
        context = self.rootContext()
        context.setContextProperty("radiomodel", self.radiomodel)
        context.setContextProperty("scrollmodel", self.scrollmodel)
        context.setContextProperty("chkmodel1", self.chkmodel1)
        context.setContextProperty("chkmodel2", self.chkmodel2)
        context.setContextProperty("chkmodel3", self.chkmodel3)
        self.load('dice/main.qml')

        #rado = self.rootObjects()[0].findChild(QObject, "radios")
        #rado.setProperty("onClicked", self.radu() )

        #layout = QVBoxLayout()
        #layout.addWidget(QPushButton('Top'))
        #layout.addWidget(QPushButton('Bottom'))
        context = QQmlContext(self.rootContext())

    def show_(self):
        if not self.rootObjects():
            return -1
        self.rootContext().setContextProperty("MainWindow", self)
        return app.exec_()



if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MainWindow()
    sys.exit(window.show_())
