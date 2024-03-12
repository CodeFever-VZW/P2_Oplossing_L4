import tkinter
from PIL import Image, ImageTk
import requests
import io


def genereer_qr_code():
    url = url_entry.get()

    if url:
        qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={url}&size=200x200"
        response = requests.get(qr_code_url)

        if response.status_code == 200:
            afbeelding_data = response.content
            qr_code_afbeelding = Image.open(io.BytesIO(afbeelding_data))

            afbeelding = ImageTk.PhotoImage(qr_code_afbeelding)
            qr_code_image_label.config(image=afbeelding)
            qr_code_image_label.image = afbeelding

        else:
            print("Er is een fout opgetreden bij het genereren van de QR-code.")


# Creëer het venster
venster = tkinter.Tk()
venster.title("QR-code Generator")
venster.geometry("300x400")
label = tkinter.Label(venster, text="Voer de URL in:")
label.pack(pady=10)
url_entry = tkinter.Entry(venster)
url_entry.pack()
generate_button = tkinter.Button(venster, text="Genereer QR-code", command=genereer_qr_code)
generate_button.pack(pady=10)
qr_code_image_label = tkinter.Label(venster)
qr_code_image_label.pack()

# Start de GUI-loop
venster.mainloop()