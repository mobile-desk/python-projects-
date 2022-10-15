#BMI CALCULATOR IN TKINTER
from tkinter import *

#function
def calculator():
    """ """
    if (w_clicked.get() == 'kg') and (h_clicked.get() == 'm'):
        l = int(height.get()) / 100
        l **= 2
        j = int(weight.get()) / l
        label.config(text= j)
    elif (w_clicked.get() == 'lb') and (h_clicked.get() == 'in'):
        l = int(height.get()) ** 2
        j = int(weight.get()) / l
        j *= 703
        label.config(text=j)
    else:
        label.config(text="FORMAT ERROR")
        exit()
    if j < 18.5:
        bmi.config(text="Underweight")
    elif 18.5 <= j < 25:
        bmi.config(text='Normal')
    elif 25 <= j < 30:
        bmi.config(text='Overweight')
    else:
        bmi.config(text='Obesity')
        



#creating GUI
root = Tk()

w_options = [
    'kg',
    'lb'
]

h_options = [
    'm',
    'in'
]

w_clicked = StringVar()
h_clicked = StringVar()

w_clicked.set('kg')
h_clicked.set('m')


w = Label(root, text="Weight")
weight = Entry(root,)
w_drop = OptionMenu(root, w_clicked, *w_options)

h = Label(root, text="Height")
height = Entry(root,)
h_drop = OptionMenu(root, h_clicked, *h_options)

button = Button(root, text='CALCULATE', command=calculator)

label = Label(root, text=" ")
bmi = Label(root, text=" ")

w.place(x=0, y=8)
weight.place(x=50, y=8)
w_drop.place(x=150, y=0)

h.place(x=0, y=58)
height.place(x=50, y=58)
h_drop.place(x=150, y=50)

button.place(x=0, y=100)
label.place(x=0, y=150)
bmi.place(x=0, y=200)

root.title("BMI CALCULATOR")
root.resizable(False, False)
root.geometry("500x500")
root.mainloop()