#!/usr/bin/python3

import alex_dice
import string

from tkinter import *
#import tkMessageBox

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   root = Tk()
   T = Text(root, height=10, width=50)
   T.config(relief=GROOVE, bd=2)

   def insertone():
       ein0.insert(END,"1")
       ein0.pack()
   def inserttwo():
       ein0.insert(END,"2")
       ein0.pack()
   def insertthree():
       ein0.insert(END,"3")
       ein0.pack()
   def insertfive():
       ein0.insert(END,"4")
       ein0.pack()
   def insertfour():
       ein0.insert(END,"5")
       ein0.pack()
   def insertsix():
       ein0.insert(END,"6")
       ein0.pack()
   def insertseven():
       ein0.insert(END,"7")
       ein0.pack()
   def inserteight():
       ein0.insert(END,"8")
       ein0.pack()
   def insertnine():
       ein0.insert(END,"9")
       ein0.pack()
   def insertten():
       ein0.insert(END,"0")
       ein0.pack()
   def insertdel():
       #ein0.insert(0," ")
       ein0.delete(0,END)
       ein0.pack()
   def insertspace():
       #ein0.insert(0," ")
       ein0.insert(END," ")
       ein0.pack()
   def einfug1():
       ein0.delete(0,END)
       ein0.insert(0, ein1.get())
   def einfug2():
       ein0.delete(0,END)
       ein0.insert(0, ein2.get())
   def einfug3():
       ein0.delete(0,END)
       ein0.insert(0, ein3.get())
   def einfug4():
       ein0.delete(0,END)
       ein0.insert(0, ein4.get())


   # BENUTZER eingabe
   Label(root, text="Default Parameter").pack(side=TOP)
   ein0 = Entry(root, bd=2, width=50)
   #ein0.insert(END, "")
   ein0.pack()

   # Eintrag 1 nutz
   #wurf = Checkbar(root, list(alex_dice.randfkt2.values()))
   wurf = Checkbar(root, list(alex_dice.randfkt2.values()))
   wurf.pack(side=LEFT,  fill=X)
   wurf.pack(side=BOTTOM)
   wurf.config(relief=GROOVE, bd=2)


   Label(root, text="Parameter Sammelung - Nr.1").pack()
   #Button(root, text='Einfuegen', command="").pack()
   ein1 = Entry(root, width=50)
   ein1.insert(END, "0 3 lin 3 2 7")
   ein1.pack()
   Button(root, text='Einfuegen', command=einfug1).pack()

   Label(root, text="Parameter Sammelung - Nr.2").pack()
   #Button(root, text='Einfuegen', command="").pack()
   ein2 = Entry(root, width=50)
   ein2.insert(END, "gewicht poly 3 2 0.7 -poly 1 2 5")
   ein2.pack()
   Button(root, text='Einfuegen', command=einfug2).pack()

   Label(root, text="Parameter Sammelung - Nr.3").pack()
   Button(root, text='Einfuegen', command=einfug3).pack()
   ein3 = Entry(root, width=50)
   ein3.insert(END, "gewicht lin 3 3 7 lin 3 3 7")
   ein3.pack()

   Label(root, text="Parameter Sammelung - Nr.4").pack()
   Button(root, text='Einfuegen', command=einfug4).pack()
   ein4 = Entry(root, width=50)
   ein4.insert(END, "gewicht lin 3 3 7 lin 3 3 7")
   ein4.pack()

   def parameterspeicher():
      f = open("paramter.cfg", "a")
      f.write(ein0.get()+"\n")
      f.write(ein1.get()+"\n")
      f.write(ein2.get()+"\n")
      f.write(ein3.get()+"\n")
      f.write(ein4.get()+"\n")
      f.close()


   def allstates():
      #print(list(lng.state()), list(tgl.state()))
      alex_dice.main("3 " + str(lng.state()) + " 3 2 7")
      T.pack()
      T.insert(END, list(lng.state()))
      T.insert(END, "\n")

   def wu():
       print(ein0.get())
       alex_dice.main(ein0.get().split())


   Button(root, text='1', command=insertone).pack(side=LEFT)
   Button(root, text='2', command=inserttwo).pack(side=LEFT)
   Button(root, text='3', command=insertthree).pack(side=LEFT)
   Button(root, text='4', command=insertfour).pack(side=LEFT)
   Button(root, text='5', command=insertfive).pack(side=LEFT)
   Button(root, text='6', command=insertsix).pack(side=LEFT)
   Button(root, text='7', command=insertseven).pack(side=LEFT)
   Button(root, text='8', command=inserteight).pack(side=LEFT)
   Button(root, text='9', command=insertnine).pack(side=LEFT)
   Button(root, text='0', command=insertten).pack(side=LEFT)
   Button(root, text='" "', command=insertspace).pack(side=LEFT)
   Button(root, text='X', command=insertdel).pack(side=LEFT)

   #Button(root, text='Wuerfeln', command=alex_dice.main("3 lin 3 2 7")).pack(side=LEFT)
   Button(root, text='Wuerfeln', command=wu).pack(side=LEFT)
   Button(root, text='Parameter speichern', command=parameterspeicher).pack(side=LEFT)

   dazu = Checkbar(root, ['an Datei anhaengen'])
   dazu.pack(side=LEFT)
   dazu.config(relief=GROOVE, bd=2)

   Button(root, text='Beenden', command=root.quit).pack(side=RIGHT)

   root.mainloop()
