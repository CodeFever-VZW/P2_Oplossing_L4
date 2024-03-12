import tkinter
from tkinter import colorchooser


def open_kleurkiezer():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        knop.config(bg=kleur)  # Je kan hier ook window gebruiken i.p.v. knop


window = tkinter.Tk()
window.title("Kleurkiezer Oefening")
window.geometry("300x200")

knop = tkinter.Button(window, text="Kies een kleur!", command=open_kleurkiezer)
knop.pack()

window.mainloop()