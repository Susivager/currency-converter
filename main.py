from turtle import *
import turtle as schildi
import time




schildi.hideturtle()
schildi.bgcolor("gray")
schildi.setup(500,300)

from turtle import Screen, Turtle

def click(x, y):
    if -40 <= x <= 40 and -20 <= y <= 20:
        turtle.write("Thank you!", align='center', font=('Arial', 18, 'bold'))





#Währungswerte etc
#CHF
chfusd = 1.05
chftry = 18.88
chfeur = 1.03
chfgbp = 0.87
chfrub = 62.79
chfbyn = 2.64







#Code

def chf(erstewährung, erstewährungzahl, zweitewährung):
    if zweitewährung == "CHF":
        schildi.write("Du kannst CHF nicht in CHF umrechnen", True, align="center")
        schildi.bgcolor("orange")
    elif zweitewährung == "TRY":
        ergebniss = erstewährungzahl * chftry
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
    elif zweitewährung == "EUR":
        ergebniss = erstewährungzahl * chfeur
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
    elif zweitewährung == "USD":
        ergebniss = erstewährungzahl * chfusd
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
    elif zweitewährung == "GPB":
        ergebniss = erstewährungzahl * chfgbp
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
    elif zweitewährung == "RUB":
        ergebniss = erstewährungzahl * chfrub
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
    elif zweitewährung == "BYN":
        ergebniss = erstewährungzahl * chfbyn
        schildi.write(ergebniss, True, align="right")
        schildi.bgcolor("green")
















ergebniss = ""

schildi.title("Währungsrechner")
erstewährung = schildi.textinput("Wähle die 1 Währung aus z.b. $, etc", "Währung:")
erstewährungzahl = schildi.numinput("Eingabe", "Umzurechnender Betrag")
zweitewährung = schildi.textinput("Eingabe", "In welche Währung willst du den Betrag umrechnen")

nil = ""

if erstewährung == "CHF":
    chf(erstewährung, erstewährungzahl, zweitewährung)
elif erstewährung == "TRY":
    print("lool")
else:
    schildi.write("Fehler: Du hast keine Gültige Währung angegeben, gültige Währungen sind: CHF EUR RUB BEL USD AND SBS DSA DSH DSA", True, align="center")
    schildi.bgcolor("red")
    schildi.setup(900, 300)






#Fehler Meldungen
if erstewährung == nil:
    #schildi.write("Fehler: Du musst eine Grundwährung angeben", True, align="center")
    schildi.bgcolor("red")
if erstewährungzahl == nil:
    schildi.write("Fehler: Du musst einen Betrag eingeben der Berechnet werden soll angeben", True, align="center")
    schildi.bgcolor("red")
if erstewährungzahl <= 0:
    schildi.write("Fehler: Der Betrag muss über 0 sein", True, align="center")
    schildi.bgcolor("red")
if zweitewährung == nil:
    schildi.write("Fehler: Du hast keine Gültige Währung angegeben in die der Betrag gerechnet werden soll, gültige Währungen sind: CHF EUR RUB BEL USD AND SBS DSA DSH DSA", True, align="center")
    schildi.bgcolor("red")
    schildi.setup(900, 300)



















































done()



