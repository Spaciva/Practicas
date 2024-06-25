import tkinter as tk
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('', "Gracias puto")
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = tk.Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = tk.Label(root, text='Eres gay??', font='Arial 20 bold', bg='white')
label.pack()

btnYes = tk.Button(root, text='no', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)

btnNo = tk.Button(root, text='Yes', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)

root.mainloop()
