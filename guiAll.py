from tkinter import *

root = Tk()
root.title('Random')
Label(text='Enter Time e.g 6:30').pack(side=TOP,padx=10,pady=10)

enterTime = Entry(root, width=10)
enterTime.pack(side=TOP,padx=10,pady=10)

Label(text='Enter Location').pack(side=TOP,padx=10,pady=10)

enterLoc = Entry(root, width=10)
enterLoc.pack(side=TOP,padx=10,pady=10)

Label(text='Enter Kind of Information').pack(side=TOP,padx=10,pady=10)

enterKind = Entry(root, width=10)
enterKind.pack(side=TOP,padx=10,pady=10)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Reg", variable = CheckVar1,
                 onvalue = "Reg", offvalue = 0)
C2 = Checkbutton(root, text = "Bp", variable = CheckVar2,
                 onvalue = "Bp", offvalue = 0)
C3 = Checkbutton(root, text = "Sugar", variable = CheckVar2,
                 onvalue = "Sugar", offvalue = 0)
C4 = Checkbutton(root, text = "Test Reports", variable = CheckVar2,
                 onvalue = "Test Reports", offvalue = 0)
C5 = Checkbutton(root, text = "Heart Test", variable = CheckVar2,
                 onvalue = "Heart Test", offvalue = 0)
C6 = Checkbutton(root, text = "Nero", variable = CheckVar2,
                 onvalue = "Nero", offvalue = 0)
C7 = Checkbutton(root, text = "Ortho", variable = CheckVar2,
                 onvalue = "Ortho", offvalue = 0)
C8 = Checkbutton(root, text = "Eye related", variable = CheckVar2,
                 onvalue = "Eye related", offvalue = 0)
C9 = Checkbutton(root, text = "Physician", variable = CheckVar2,
                 onvalue = "Physician", offvalue = 0)


C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
C6.pack()
C7.pack()
C8.pack()
C9.pack()

def onok():
    x, y = enterTime.get().split(':')
    p=enterLoc.get()
    q=enterKind.get()
    z = int(str(x) + str(y))
    print(p,q,z)



Button(root, text='OK', command=onok).pack(side=LEFT)
# Button(root, text='CLOSE').pack(side= RIGHT)

root.mainloop()
