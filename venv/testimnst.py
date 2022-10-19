import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json

s = s

root = tk.Tk()
root.title("Währungsrechner")
root.geometry("500x600")
root.resizable(width=False, height=False)



#Funktions
def berechnen():
    currency1 = entry1.get()
    currency2 = entry2.get()
    amount = entry3.get()

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
    resultrequest = response.text
    result = json.loads(resultrequest)
    ttk.Label(root, text=result["result"]).pack()




#Texte
label1 = tk.Label(root, text="Umzurechnende Währung", height=2)
label2 = tk.Label(root, text="Zielwährung", height=2)
label3 = tk.Label(root, text="Betrag", height=2)

#Leere
leer1 = tk.Label(root, text="", height=1)
leer2 = tk.Label(root, text="", height=1)
#Eingaben
entry1 = ttk.Entry(root, width=70)
entry2 = ttk.Entry(root, width=70)
entry3 = ttk.Entry(root, width=70)
#Buttons
button1 = ttk.Button(root, text="Berechnen", command=berechnen)

#Pack
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
leer1.pack()
button1.pack()
leer2.pack()











root.mainloop()