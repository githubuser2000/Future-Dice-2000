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
    @pyqtSlot()
    def wuerfeln2(self):
        result = dice.wuerfeln()
        print("r " + str(result) )
        for ell in result:
            for i,el in enumerate(ell):
                self.scrollmodel.insertPerson(i, str(el), True)
    @pyqtSlot()
    def wuerfelErstellen(self):
        wuerfe = self.rootObjects()[0].findChild(QObject, "wuerfe")
        n = self.rootObjects()[0].findChild(QObject, "n")
        x = self.rootObjects()[0].findChild(QObject, "x")
        y = self.rootObjects()[0].findChild(QObject, "y")
        augen = self.rootObjects()[0].findChild(QObject, "augen")
        sview = self.rootObjects()[0].findChild(QObject, "scrollView")
        print("x")
        #wuerfe.setProperty("text", "x" )
        print(wuerfe.property("text"))
        print(wuerfe.property("text"))
        result = dice.main(['dicegui',augen.property("text"),'lin',n.property("text"),x.property("text"),y.property("text")],int(wuerfe.property("text")), False)
        for ell in result:
            for i,el in enumerate(ell):
                self.scrollmodel.insertPerson(i, str(el), True)
    def __init__(self):
        super().__init__()
        radiomodel = model2.PersonModel()
        self.scrollmodel = model2.PersonModel()
        for i,el in enumerate(list(dice.randfkt2.values())):
            radiomodel.insertPerson(i, el, True if i==0 else False)
        context = self.rootContext()
        context.setContextProperty("radiomodel", radiomodel)
        context.setContextProperty("scrollmodel", self.scrollmodel)
        self.load('dice/main.qml')

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
