#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math
import random
    #from collections import defaultdict
    # argv
    # 1 ist würfel bis zahl
    # 2 ist lin log root etc
    # zahl n, bei lin zB Schrittweite
    # zahl die definiert werden sein soll z.B. 5 Augen als kurz vor Maximum
    # sys.argv
randfkt2 = { 1 : 'lin',
            2 : 'log',
            3 : 'root',
            4 : 'poly',
            5 : 'exp',
            6 : 'kombi',
            7 : 'logistic',
            8 : 'rand',
            9 : 'gewicht'}

randfkt3 = { 1 : 'mul',
            2 : 'add',
            3 : 'log',
            4 : 'root'}
class dice():

    def sigmoid(self,x,n,xe,e,xth=0):
        x-=int(self.inpp_[1])/2
        xe-=int(self.inpp_[1])/2
        return ( n / (n + math.exp(-x)) ) / ( n / (n + math.exp(-xe)) ) * e

    def lin(self,x,n,xe,e,xth=0):
        #print(str(x))
        #print(str(e))
        #print(str(xe))
        return (x * e) / xe
    def log(self,x,n,xe,e,xth=0):
        return math.log(x,n) / math.log(xe,n) * e
    def root(self,x,n,xe,e,xth=0):
        return pow(x,1/n) / pow(xe,1/n) * e
    def poly(self,x,n,xe,e,xth=0):
        return pow(x,n) / pow(xe,n) * e
    def expo(self,x,n,xe,e,xth=0):
        return pow(n,x) / pow(n,xe) * e

    def randselect(self,includex):

            d = 1000

            #print("CC "+str((includex)))
            if not len(includex) == 4:
                flag1 = False
                for i,inc in enumerate(includex):
                    if self.randfkt[i+1].__name__ == "kombi":
                        pass
                    elif self.randfkt[i+1].__name__ == "gewicht":
                        pass
                    elif self.randfkt[i+1].__name__ == "rand":
                        pass
                    elif inc:
                        flag1 = True
                if not flag1:
                    return 1
                self.randfktvarx = random.randrange(len(includex))+1

                while not includex[self.randfktvarx-1] or self.randfkt[self.randfktvarx].__name__ == "gewicht":
                    d-=1
                    if d <= 0:
                        return 1
                    self.randfktvarx = random.randrange(len(includex))+1
                return self.randfktvarx
            else:
                flag1 = False
                for i,inc in enumerate(includex):
                    if inc:
                        flag1 = True
                if flag1:
                    self.randfktvarx = random.randrange(len(includex))+1
                    while not includex[self.randfktvarx-1]:
                        d-=1
                        if d <= 0:
                            return 1
                        self.randfktvarx = random.randrange(len(includex))+1
                    #print("BB "+str(self.randfktvarx))
                    return self.randfktvarx
                else:
                    #print("AA 1")
                    return 1

    def kombi(self,x,n,xe,e,xth=0, reku = 50):
        try:
        #if True:
#            okay1 = False
#            okay2 = False
#            for i,k in zip(self.include1,self.include2):
#                if i:
#                    okay1 = True
#                if k:
#                    okay2 = True
#
            #if not okay1 or not okay2:
            #    return None
            self.randfktvar1,self.randfktvar2,self.randfktvar3 = self.randselect(self.include1),self.randselect(self.include2),self.randselect(self.include3)
            #print("-- "+str(self.randfktvar1)+" "+str(self.randfktvar2)+" "+str(self.randfktvar3))

            if self.randfktvar3 == 1:
                print("Kombi Mulitply: "+str(randfkt2[self.randfktvar1])+" "+str(randfkt2[self.randfktvar2]))
                return self.randfkt[self.randfktvar1](x,n,xe,e) * self.randfkt[self.randfktvar2](x,n,xe,e)
            elif self.randfktvar3 == 2:
                print("Kombi Addition "+str(randfkt2[self.randfktvar1])+" "+str(randfkt2[self.randfktvar2]))
                return self.randfkt[self.randfktvar1](x,n,xe,e) + self.randfkt[self.randfktvar2](x,n,xe,e)
            elif self.randfktvar3 == 3:
                print("Kombi Logarithm "+str(randfkt2[self.randfktvar1])+" "+str(randfkt2[self.randfktvar2]))
                return math.log(self.randfkt[self.randfktvar1](x,n,xe,e)+1.1,self.randfkt[self.randfktvar2](x,n,xe,e)+1.1)
            elif self.randfktvar3 == 4:
                print("Kombi Root "+str(randfkt2[self.randfktvar1])+" "+str(randfkt2[self.randfktvar2]))
                return pow(self.randfkt[self.randfktvar1](x,n,xe,e), 1 / ( self.randfkt[self.randfktvar2](x,n,xe,e) + 1 ))
        except:
            if reku > 0:
                reku -= 1
                return self.kombi(x,n,xe,e,xth,reku)

    def gewicht(self,type1,x,n,xe,e,type2,n2,xe2,e2):
        return ( self.fkt[type1](x,n,xe,e),
                self.fkt[type2](x,n2,xe2,e2,1) )


    def rand(self,x,n,xe,e,xth=0):
        okay1 = False
        for i in self.include1:
            if i:
                okay1 = True
        if not okay1:
            return 1
        self.randfktvarA = self.randselect(self.include1 if xth == 0 else self.include2)
        result = self.randfkt[self.randfktvarA](x,n,xe,e,xth)
        return result



    def weightedrand(self,weights):
        print("ww "+str(weights))
        summ = 0
        sum2 = []
        for weight in weights:
            summ += weight
            sum2.append(summ)

        rand1 = random.random() * summ

        for i,asum in enumerate(sum2):
            if rand1 < asum:
                return i # +1

        return None



    def help(self):
        print("dice.py 3 -lin 3 2 7")
        print("dice.py 3 gewicht poly 3 2 0.7 -poly 1 2 5")
        print("dice.py 3 gewicht lin 3 3 7 lin 3 3 7")
        print("dice.py 3 kombi 3 3 0.7")
        print("dice.py 3 rand 3 3 5")

    #self.randos, self.wuerfelType, self.wuerfelWuerfe, self.uniq, self.values = None, None, None, None, None


    def wuerfeln(self):
        self.wuerfelWuerfe2 = []
        if len(self.wuerfelAugenSet) == len(self.randos):
            self.wuerfelAugenSet = set()
        if self.wuerfelType == 0:
            while True:
                dice = random.randrange(len(self.randos))
                if not dice in self.wuerfelAugenSet or not self.uniq:
                    self.wuerfelAugenSet.add(dice)
                    break
            self.wuerfelWuerfe2.append((dice,self.randos[dice],self.bezeichners[dice]))
            self.wuerfelWuerfe.append((dice,self.randos[dice],self.bezeichners[dice]))
            print("Würfelwurf: "+str(self.randos[dice])+" (Würfelaugen "+str(dice+1)+")")
        elif self.wuerfelType == 1:
            while True:
                dice = self.weightedrand(self.randos)
                if not dice in self.wuerfelAugenSet or not self.uniq:
                    self.wuerfelAugenSet.add(dice)
                    break
            print("rand augenzahl ergebnis: "+str(dice))
            #dice = random.randrange(inp[1])+1
            #ergebnis = (self.randos[dice],self.values[dice])
            ergebnis = (self.values[dice],self.randos[dice])
            self.wuerfelWuerfe2.append((dice,ergebnis[0],ergebnis[1],self.bezeichners[dice]))
            self.wuerfelWuerfe.append((dice,ergebnis[0],ergebnis[1],self.bezeichners[dice]))
            print("Würfelwurf: "+str(self.randos[dice])+" (Würfelaugen "+str(dice)+")")
        return self.wuerfelWuerfe2

    def __init__(self,inp,werfen = 2, uniq_ = False, bezeichner : str = "", negativ = False, median = False):
        self.negativ = negativ
        self.median = median
        self.bezeichner = bezeichner
        self.wuerfeltype = None
        self.wuerfelAugenSet = set()
        self.fkt = { 'lin' : self.lin,
            'log' : self.log,
            'root' : self.root,
            'poly' : self.poly,
            'exp' : self.expo,
            'rand' : self.rand,
            'kombi' : self.kombi,
            'gewicht' : self.gewicht,
            '-lin' : self.lin,
            '-log' : self.log,
            '-root' : self.root,
            '-poly' : self.poly,
            '-exp' : self.expo,
            '-rand' : self.rand,
            '-kombi' : self.kombi,
            'logistic' : self.sigmoid,
            '-logistic' : self.sigmoid}



        self.randfkt = { 1 : self.lin,
            2 : self.log,
            3 : self.root,
            4 : self.poly,
            5 : self.expo,
            6 : self.kombi,
            7 : self.sigmoid,
            8 : self.rand,
            9 : self.gewicht}


        #randfkt2 = { 1 : 'lin',
        #    2 : 'log',
        #    3 : 'root',
        #    4 : 'poly',
        #    5 : 'exp',
        #    6 : 'kombi',
        #    7 : 'logistic',
        #    8 : 'rand',
        #    9 : 'gewicht'}
#
#        randfkt3 = { 1 : 'mul',
#            2 : 'add',
#            3 : 'log',
#            4 : 'root'}
        self.inpp_ = inp
        self.wuerfelWuerfe = werfen
        self.uniq =uniq_
        self.wuerfelWuerfe = []
        self.wuerfelWuerfeMoeglichkeiten = {}

        self.bezeichners = str(bezeichner).split()
        if not self.bezeichner == "":
            while len(self.bezeichners) < int(inp[1]):
                self.bezeichners.append("?")
        else:
            while len(self.bezeichners) < int(inp[1]):
                self.bezeichners.append("")
        #if len(self.bezeichners) > 0:
        #    if self.bezeichners[-1] == "?":
        #        self.bezeichner = " ".join(self.bezeichners)

        if len(inp) > 3:
            if type(inp[-3]) is list and type(inp[-2]) is list and type(inp[-1]) is list:
                self.include1,self.include2,self.include3 = inp[-3],inp[-2],inp[-1]
                #print('_'+str(self.include3))
                inp=inp[:-3]
            else:
                i1,i2,i3 = [],[],[True,True,True,True]
                for i in range(len(randfkt2)):
                    i1.append(True)
                    i2.append(True)
                self.include1,self.include2,self.include3 = i1,i2,i3
        if len(inp) == 6:
            until = int(inp[1])
            inp[4] = int(inp[4])
            inp[5] = float(inp[5])
            inp[3] = float(inp[3])
            inp[1] = int(inp[1])
            #print("UU-"+str(inp[1])+" "+str(inp[4])+" ")
            if inp[4] <= inp[1] and inp[4] > 1 and inp[2] != "gewicht":
                self.randos = []
                for a in range(1,until+1):
                    self.randos.append(self.fkt[inp[2]](a,inp[3],inp[4],inp[5]))
                if inp[2][0]=='-':
                    self.randos.reverse()
                for i,(value, bezeich) in enumerate(zip(self.randos,self.bezeichners)):
                    self.wuerfelWuerfeMoeglichkeiten[i] = [value, bezeich]
                    print(str(i+1)+": "+str(value))
                self.wuerfelType = 0
        elif len(inp) == 11 and inp[2] == "gewicht":
            #print("d")
            until = int(inp[1])
            inp[4] = int(inp[4])
            inp[5] = int(inp[5])
            inp[6] = float(inp[6])
            inp[1] = int(inp[1])
            inp[8] = float(inp[8])
            inp[9] = int(inp[9])
            inp[10] = float(inp[10])
            if inp[5] <= inp[1] and inp[5] > 0 and inp[9] <= inp[1] and inp[9] > 0:
                self.values = []
                self.randos = []
                for a in range(1,until+1):
                    thing = self.fkt['gewicht'](inp[3],a,inp[4],inp[5],inp[6],inp[7],inp[8],inp[9],inp[10])
                    self.values.append(thing[0])
                    self.randos.append(thing[1])
                if inp[3][0]=='-':
                    self.values.reverse()
                if inp[7][0]=='-':
                    self.randos.reverse()
                for i,(rando,value,bezeich) in enumerate(zip(self.values,self.randos,self.bezeichners)):
                    self.wuerfelWuerfeMoeglichkeiten[i] = [rando,value,bezeich]
                    print(str(i+1)+": "+str(value))
                    print(str(i+1)+": "+str(rando)+", "+str(value))
                self.wuerfelType = 1
        else:
            self.help()
            return None
        if self.negativ:
            #avg = 0
            #for key,wert in self.wuerfelWuerfeMoeglichkeiten.items():
            #    avg += float(wert[len(self.wuerfelWuerfeMoeglichkeiten)- 2])
            #avg = avg / len(self.wuerfelWuerfeMoeglichkeiten)
            self.randos= []
            middle = self.wuerfelWuerfeMoeglichkeiten[int(len(self.wuerfelWuerfeMoeglichkeiten)/2)][0]
            for key,wert in self.wuerfelWuerfeMoeglichkeiten.items():
                #print("p "+str(self.wuerfelWuerfeMoeglichkeiten[int(len(self.wuerfelWuerfeMoeglichkeiten)/2)][0]))
                #print("p "+str((self.wuerfelWuerfeMoeglichkeiten[key])))
                #print(self.wuerfelWuerfeMoeglichkeiten[int(len(self.wuerfelWuerfeMoeglichkeiten)/2)][len(self.wuerfelWuerfeMoeglichkeiten[0])- 2])
                #print(str(self.wuerfelWuerfeMoeglichkeiten[int(len(self.wuerfelWuerfeMoeglichkeiten)/2)][len(self.wuerfelWuerfeMoeglichkeiten)- 2]))
                wert[0] -= middle
                self.randos.append(wert[0])
        for i in range(werfen):
            self.wuerfelWuerfe.append(self.wuerfeln())
        self.result = (self.wuerfelWuerfeMoeglichkeiten,self.wuerfelWuerfe)
        print(str(self.result))

    def out(self):
        return self.result


    #if len(sys.argv) > 5:
    #    main(sys.argv)
    #else:
    #    self.help()
