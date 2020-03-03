#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent, QQmlContext
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys
#from PyQt5 import QtCore
from PyQt5.QtQuick import QQuickView, QQuickItem
from PyQt5.QtCore import QObject, QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot, QUrl, QTranslator, QLocale
import libdice
import model2
import locale

class MainWindow(QQmlApplicationEngine):
    wuerfelrestellt = False
#    radi = 'lin'

    #@pyqtSlot()
    #def getRadioBselected(self):
        #print(str(self.radi))
        #radios = self.rootObjects()[0].findChild(QObject, "radiolayout")
        #print(radios.property["objectName"])
        #for i,radio in enumerate(radios.children()):
        #    print(str(radio.property("text")))
        #    print(str("x"+str(radio.property("checked"))))
        #    if radio.property("checked"):
        #        print(dice.randfkt2[i+1])

    def insertresults(self,result):
        if self.gesamtgewicht == None:
            self.gesamtgewicht = 0
            #print('res '+str(result))
            for i,oneOf2 in enumerate(result):
                if type(oneOf2) is dict:
                    for k,(key, value) in enumerate(oneOf2.items()):
                        if len(value) >= 3:
                            self.gesamtgewicht += float(value[1])
                            #print(str("add "+str(float(value[1]))))
        if self.gesamtgewicht == 0:
            self.gesamtgewicht = 1

        self.wurflist.append(result)

        for i,oneOf2 in enumerate(result):
#            for i,elo in enumerate(ell):
#                for i,el in enumerate(elo):
            str_augen = self.tr('Augen ')
            str_wert = self.tr(' Wert ')
            str_gewicht = self.tr(', Gewicht: ')
            str_wurf = self.tr('Wurf ')
            if type(oneOf2) is dict:
                self.scrollmodel.insertPerson(0, '', True,'')
                for k,(key, value) in enumerate(oneOf2.items()):
                    if type(value) in [tuple,list]:
                        if len(value) == 3:
                            self.scrollmodel.insertPerson(0, str_augen+str(key+1)+". ("+str(value[2])+"):"+str_wert+locale.str(round(float(value[0])*100)/100)+str_gewicht+locale.str(round(float(value[1])*100)/100)+" "+str(int(float(value[1]/self.gesamtgewicht*100)))+"%", True,'')
                        elif len(value) == 2:
                            self.scrollmodel.insertPerson(0, str_augen+str(key+1)+". ("+str(value[1])+"):"+str_wert+locale.str((round(float(value[0])*100))/100), True,'')
                self.scrollmodel.insertPerson(0, '', True,'')
        for i,oneOf2 in enumerate(result):
            if  type(oneOf2) in [tuple] and len(oneOf2) in [3,4]:
                self.wuerfe += 1
                if len(oneOf2) == 4:
                    self.wurfnummer += 1
                    self.scrollmodel.insertPerson(0, str_wurf+str(self.wurfnummer)+". "+((str_augen+str(int(oneOf2[0])+1)+".") if oneOf2[3]=="" else oneOf2[3])+str_wert+locale.str(round(float(oneOf2[1])*100)/100)+str_gewicht+locale.str(round(float(oneOf2[2])*100)/100)+" "+str(int(float(oneOf2[2]/self.gesamtgewicht*100)))+"%", True,'')
                elif len(oneOf2) == 3:
                    self.wurfnummer += 1
                    self.scrollmodel.insertPerson(0, str_wurf+str(self.wurfnummer)+". "+((str_augen+str(int(oneOf2[0])+1)+".") if oneOf2[2]=="" else oneOf2[2])+str_wert+locale.str(oneOf2[1]), True,'')
            elif  type(oneOf2) is list:
                for k,erstwuerfe in enumerate(oneOf2):
                    #if  len(erstwuerfe) in [3,4] and type(erstwuerfe) in [tuple,list]:
                    self.wuerfe += 1
                    if len(erstwuerfe) == 4:
                        self.wurfnummer += 1
                        self.scrollmodel.insertPerson(0, str_wurf+str(self.wurfnummer)+". "+((str_augen+str(int(erstwuerfe[0])+1)+".") if erstwuerfe[3]=="" else erstwuerfe[3])+str_wert+locale.str(round(float(erstwuerfe[1])*100)/100)+str_gewicht+locale.str(round(float(erstwuerfe[2])*100)/100)+" "+str(int(float(erstwuerfe[2]/self.gesamtgewicht*100)))+"%", True,'')
                    elif len(erstwuerfe) == 3:
                        self.wurfnummer += 1
                        self.scrollmodel.insertPerson(0, str_wurf+str(self.wurfnummer)+". "+((str_augen+str(int(erstwuerfe[0])+1)+".") if erstwuerfe[2]=="" else erstwuerfe[2])+str_wert+locale.str(round(float(erstwuerfe[1])*100)/100), True,'')

    @pyqtSlot()
    def uniq(self):
        if hasattr(self,'dice'):
            self.dice.uniq = bool(self.rootObjects()[0].findChild(QObject, "uniq").property("position"))


    @pyqtSlot()
    def wuerfeln2(self):
        #print(str(self.radios.property("checksate")))
        self.lastWuerfelungen = []
        if not self.wuerfelrestellt:
            self.wuerfelErstellen()
        else:
            wuerfe = self.rootObjects()[0].findChild(QObject, "wuerfe")
            for i in range(int(wuerfe.property("text"))):
                result = self.dice.wuerfeln()
                #print("r " + str(result) )
                self.insertresults(result)
                self.lastWuerfelungen.append(result)
#                for ell in result:
#                    for i,el in enumerate(ell):
#                        self.scrollmodel.insertPerson(i, str(el), True)
    def checkedchanged(self):
        Lists=[]
        for checkgroups in ["_LCheck1_","_LCheck2_", "_LCheck3_"]:
            ListChecked = self.rootObjects()[0].findChild(QObject, checkgroups)
            changedchecked = ListChecked.property("anObject").toVariant()
            #print(str(changedchecked))
            checklist=[]
            for key0,key1 in (libdice.dice.randfkt2.items() if not checkgroups == "_LCheck3_" else libdice.dice.randfkt3.items()):
                for key2,value2 in changedchecked.items():
                    if key2 == key1:
                        checklist.append(value2)
            Lists.append(checklist)
        #print(str(Lists))
        return Lists


    @pyqtSlot()
    def wuerfelErstellen(self):
        self.wurflist = []
        self.gesamtgewicht = None
        Lists = self.checkedchanged()
        self.wuerfelrestellt = False
        if not self.wuerfelrestellt:
            self.wurfnummer = 0
            self.gesamtgewicht = None
            self.wuerfe = 0
            self.wuerfelrestellt = True
            wuerfe = self.rootObjects()[0].findChild(QObject, "wuerfe")
            n2 = self.rootObjects()[0].findChild(QObject, "n2")
            x2 = self.rootObjects()[0].findChild(QObject, "x2")
            y2 = self.rootObjects()[0].findChild(QObject, "y2")
            n = self.rootObjects()[0].findChild(QObject, "n")
            x = self.rootObjects()[0].findChild(QObject, "x")
            y = self.rootObjects()[0].findChild(QObject, "y")
            planesNames = self.rootObjects()[0].findChild(QObject, "WürfFlächBenennungen")
            augen = self.rootObjects()[0].findChild(QObject, "augen")
            sview = self.rootObjects()[0].findChild(QObject, "scrollView")
            uniq = self.rootObjects()[0].findChild(QObject, "uniq")
            reverse = self.rootObjects()[0].findChild(QObject, "reverse")
            reverse2 = self.rootObjects()[0].findChild(QObject, "reverse2")
            #print("x "+str(uniq.property("position"))+" x "+str(reverse.property("position")))
            #wuerfe.setProperty("text", "x" )
            LRad = self.rootObjects()[0].findChild(QObject, "LRad")
            LRad2 = self.rootObjects()[0].findChild(QObject, "LRad2")
            ListChecked1 = self.rootObjects()[0].findChild(QObject, "_LCheck1_")
            nega_ = self.rootObjects()[0].findChild(QObject, "nega_")
            medi_ = self.rootObjects()[0].findChild(QObject, "medi_")
            #print("u"+ str(ListChecked1.property("anObject").toVariant()))
            #ListChecked2 = self.rootObjects()[0].findChild(QObject, "repeatercheck2")
            #ListChecked3 = self.rootObjects()[0].findChild(QObject, "repeatercheck3")
            gezinkt = True if self.rootObjects()[0].findChild(QObject, "gewicht").property("position") == 1 else False
            #print(str(blub))
            #print(str(self.rootObjects()[0].findChild(QObject, "gewicht").property("position")))
            #print(str(self.radiogroup))
            #print(str(self.radiogroup.property("ButtonGroup")))
            #priint(wuerfe.property("text"))

            #print(wuerfe.property("text"))
            result = None
            #augen.property("text")
            #reverse.property("position")
            #LRad.property("text")
            #n.property("text")
            #x.property("text")
            #y.property("text")
            #uniq.property("position")
            #wuerfe.property("text")
            #print('ü '+str(gezinkt)+' '+str(['dicegui',augen.property("text"),('-' if reverse.property("position")==1 else '' )+LRad.property("text"),n.property("text"),x.property("text"),y.property("text")] + Lists))
            #print("__ "+LRad2.property("text")+" "+str(Lists))
            if not gezinkt:
                self.dice = libdice.dice(['dicegui',augen.property("text"),('-' if reverse.property("position")==1 else '' )+LRad.property("text"),n.property("nn"),x.property("text"),y.property("nn")] + Lists,int(wuerfe.property("text")), True if uniq.property("position")==1 else False,planesNames.property("text").strip() if planesNames.property("sett") else "",nega_.property("checked"),medi_.property("checked"))
            else:
                self.dice = libdice.dice(['dicegui',augen.property("text"),'gewicht',('-' if reverse.property("position")==1 else '' )+LRad.property("text"),n.property("nn"),x.property("text"),y.property("nn"),('-' if reverse2.property("position")==1 else '' )+LRad2.property("text"),n2.property("nn"),x2.property("text"),y2.property("nn")] + Lists,int(wuerfe.property("text")), True if uniq.property("position")==1 else False,planesNames.property("text").strip() if planesNames.property("sett") else "",nega_.property("checked"),medi_.property("checked"))
            self.insertresults(self.dice.out())
#            for ell in result:
#                for i,el in enumerate(ell):
#                    self.scrollmodel.insertPerson(i, str(el), True)
    def __init__(self,app):
        super().__init__()
        self.app = app
        libdice.dice.languages(app,self)

        self.radiomodel1 = model2.PersonModel()
        self.radiomodel2 = model2.PersonModel()
        self.scrollmodel = model2.PersonModel()
        self.chkmodel1,self.chkmodel2,self.chkmodel3 = model2.PersonModel(),model2.PersonModel(),model2.PersonModel()
        for i,el in enumerate(list(libdice.dice.randfkt2.values())[:-1]):
            self.radiomodel1.insertPerson(i, el, True if i==0 else False, 'radio1'+el)
            self.radiomodel2.insertPerson(i, el, True if i==0 else False, 'radio2'+el)
            self.chkmodel1.insertPerson(i, el, True, 'chk1'+el)
            self.chkmodel2.insertPerson(i, el, True, 'chk2'+el)
        for i,el in enumerate(list(libdice.dice.randfkt3.values())):
            self.chkmodel3.insertPerson(i, el, True,'chk3'+el)
        context = self.rootContext()
        context.setContextProperty("radiomodel1", self.radiomodel1)
        context.setContextProperty("radiomodel2", self.radiomodel2)
        context.setContextProperty("scrollmodel", self.scrollmodel)
        context.setContextProperty("chkmodel1", self.chkmodel1)
        context.setContextProperty("chkmodel2", self.chkmodel2)
        context.setContextProperty("chkmodel3", self.chkmodel3)
        self.load('main.qml')

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
    app.setWindowIcon(QIcon("wuerfel.png"));
    window = MainWindow(app)
    sys.exit(window.show_())
