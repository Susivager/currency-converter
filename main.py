import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json
from winotify import Notification


##################################################################################
#                      Währungsrechner by Simon                                  #
#                             Informationen                                      #
# Der Rechner wird am besten auf einem Windows System verwendet da sonst einige  #
# Funktionen wie die Benachrichtigungen nicht Funktionieren. Dazu muss die Datei #
#         waehrungen.txt im gleichen Ordner wie die main.py sein.                #
#                                                                                #
##################################################################################





#TKinter Fenster Einstellungen
root = tk.Tk()
root.title("Währungsrechner")
root.geometry("500x325")
root.resizable(width=False, height=False)

#Funktions


def währunganzeigen():  #Funktion gibt die Verschiedenen Währungen aus in dem Sie die Datei waehrungen.txt öffnet liest und dann das gelesene in die Konsole schreibt
    print("Lolipop")
    notify = Notification(app_id="Währungsrechner",
                         title="Alle Verfügbaren Währungen",
                         msg="Schaue in die Kommando Zeile um alle Währungen Einzusehen",
                         icon=r"c:\desktop\logo\icon.png")
    notify.show()
    datei = open('waehrungen.txt', 'r')
    print(datei.read())





def berechnen(): #Funktion holt sich von der API Exchangerates (https://apilayer.com/marketplace/exchangerates_data-api)
                 #Mit den Daten die vorher eingegeben wurden die umgerechnete Summe und gibt diese aus. Falls jedoch keine Summe
                 #Sondern ein Error Code zurückgegeben wird zeigt es eine Meldung an das man etwas falsch eingegeben hat.
    currency1 = entry1.get()
    currency2 = entry2.get()
    amount = entry3.get()
#Ab hier Code von https://apilayer.com/marketplace/exchangerates_data-api
    url = "https://api.apilayer.com/exchangerates_data/convert?to=" + str(currency2) \
          + "&from=" + str(currency1) \
          + "&amount=" + str(amount) \
          + ""
    payload = {}
    headers = {
        "apikey": "mU6bap1imPwGt4R9RU6xwXwDHg1EFVYn"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
#Bis hier Code von https://apilayer.com/marketplace/exchangerates_data-api
    if status_code == 400:
        messagebox.showerror("Warnung", "Achtung du hast eine nicht existente Währung angegeben oder eine ungültige angabe bei der Summe angegeben")
    resultrequest = response.text
    result = json.loads(resultrequest)
    resultat = result["result"]
    lösunganzeigen.config(text=resultat)
    notify = Notification(app_id="Währungsrechner",
                         title="Das Resutat in " + currency2,
                         msg=resultat,
                         icon=r"c:\desktop\logo\icon.png")
    notify.show()





#Texte
label1 = tk.Label(root, text="Umzurechnende Währung", height=2)
label2 = tk.Label(root, text="Betrag", height=2)
label3 = tk.Label(root, text="Zielwährung", height=2)

#Leere
leer1 = tk.Label(root, text="", height=1)
leer2 = tk.Label(root, text="", height=1)
#Eingaben
entry1 = ttk.Entry(root, width=70)
entry2 = ttk.Entry(root, width=70)
entry3 = ttk.Entry(root, width=70)
#Buttons
button1 = ttk.Button(root, text="Berechnen", command=berechnen)
button2 = ttk.Button(root, text="Währungen anzeigen", command=währunganzeigen)

##Lösung
Resultat = tk.Label(root, text="Resultat", height=-1)
lösunganzeigen = tk.Label(root, text="", height=-1)

#Packen der TK inter Labels, Entrys und Buttons
label1.pack()
entry1.pack()
label2.pack()
entry3.pack()
label3.pack()
entry2.pack()
leer1.pack()
button1.pack()
leer2.pack()
Resultat.pack()
lösunganzeigen.pack()
button2.pack()











root.mainloop()