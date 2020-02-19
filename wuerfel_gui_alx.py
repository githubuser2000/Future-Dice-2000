#!/usr/bin/python3

import alex_dice

from tkinter import *
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
   lng = Checkbar(root, ['-', 'lin', 'log', 'root', 'poly', 'expo', 'rand', 'kombi', 'gewicht'])
   tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)
   T.config(relief=GROOVE, bd=2)

   def allstates():
      #print(list(lng.state()), list(tgl.state()))
      T.pack()
      liste = list(lng.state())
      liste.append("\n")
      T.insert(END, liste )
#      T.insert(END, "\n")

   Button(root, text='Beenden', command=root.quit).pack(side=LEFT)
   Button(root, text='Wuerfeln', command=allstates).pack(side=LEFT)
   #T.pack()
   #T.insert(END, "Just a text Widget\nin two lines\n")
   #T.config(relief=GROOVE, bd=2)
   root.mainloop()
