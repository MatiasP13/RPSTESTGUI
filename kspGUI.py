from tkinter import *
from tkinter import ttk
import random

def odabir_slike():
    pass

def odabir_racunala():
    pass

def igraj(odabir_igraca):
    pass

def pobjednik(igrac, protivnik):
    pass

root = Tk()
root.title("Igra KSP")
root.geometry("480x400")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, S, E))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

label_uputa_korisniku = ttk.Label(mainframe, text = 'Klikni na sliku da odabereš').grid(column = 2, row = 2, sticky = (W))

#kamen
slika_kamen = PhotoImage(file = 'rock.png')
button_kamen = ttk.Button(mainframe, image = slika_kamen, command = lambda odabir_igraca = 'k' : igraj(odabir_igraca))
button_kamen.grid(column = 1, row = 1, sticky = (W))

#skare
slika_skare = PhotoImage(file = 'scissors.png')
button_skare = ttk.Button(mainframe, image = slika_skare, command = lambda odabir_igraca = 's' : igraj(odabir_igraca))
button_skare.grid(column = 2, row = 1, sticky = (W))

#papir
slika_papir = PhotoImage(file = 'paper.png')
button_papir = ttk.Button(mainframe, image = slika_papir, command = lambda odabir_igraca = 'p' : igraj(odabir_igraca))
button_papir.grid(column = 3, row = 1, sticky = (W))

root.mainloop()