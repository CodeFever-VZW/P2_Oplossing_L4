import tkinter
from tkinter import messagebox


def toon_bericht():
    messagebox.showinfo("Informatie", "Dit is een berichtbox!")

# Nieuw Tkinter-window
window = tkinter.Tk()
window.title("Voorbeeld van Berichtbox")

# Knop om het berichtvenster te tonen
knop = tkinter.Button(window, text="Toon Bericht", command=toon_bericht)
knop.pack()

# Start de Tkinter-eventloop
window.mainloop()