from tkinter import *

root = Tk()

hh = ""
def replaces():
    word = b.get()
    rep = d.get()
    new = g.get()
    global hh
    hh = word.replace(rep, new)
    print(hh)
    jj["text"] = hh


a = Label(root, text="Input")
b = Entry(root,)
c = Label(root, text="what do you wanna replace")
d = Entry(root,)
e = Label(root, text="what do you wanna change it to")
g = Entry(root)
f = Button(root, text="Replace", command=replaces)
jj = Label(root, text='', font=(50))

a.place(x=0, y=0)
b.place(x=0, y=30)
c.place(x=0, y = 60)
d.place(x=0, y=90)
e.place(x=0, y=120)
g.place(x=0, y=150)
f.place(x=0, y=180)
jj.place(x=0, y=210)


root.mainloop()