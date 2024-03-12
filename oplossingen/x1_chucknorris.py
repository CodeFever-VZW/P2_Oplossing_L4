import tkinter
import requests


def toon_chuck_norris_grap():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        data = response.json()
        grap_label.config(text=data["value"])
    else:
        grap_label.config(text="Er is een probleem opgetreden bij het ophalen van de grap.")


app = tkinter.Tk()
app.title("Chuck Norris Grappen")
app.geometry("800x200")

knop = tkinter.Button(app, text="Toon Chuck Norris Grap", command=toon_chuck_norris_grap)
knop.pack(pady=20)

grap_label = tkinter.Label(app, text="", wraplength=600)
grap_label.pack()

app.mainloop()