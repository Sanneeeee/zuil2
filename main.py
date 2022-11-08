import random
import requests
import json
import psycopg2
from datetime import datetime#voor het krijgen van de datum en tijd
from tkinter import *


def wegschrijven(bericht):
    """
    checkt de naam en voegt alles(naam, bericht, datum, tijd en locatie) samen om dit naar txt file te sturen.
    :param bericht: het bericht van de reiziger heeft achtergelaten
    :return:
    """
    naamNewLine = naamtext.get("1.0", END)

    naamlst=naamNewLine.split('\n')    #haalt de \n erachter weg
    naam = naamlst[0]
    berichtlst=bericht.split('\n')
    bericht = berichtlst[0]
    # lst=[naam,bericht]
    # print(lst)


    if naam == '' or naam == '.' or naam == ' ':  # als naam niet is ingevuld word naam 'anoniem'
        naam = 'anoniem'

    now = datetime.now()          #tijd van het bericht
    dateTime = now.strftime("%d/%m/%Y %H:%M:%S")


    randomLocatie = ['Utrecht', 'Assen', 'Zwolle', 'Groningen']  # bepaling van de locatie
    locatie = random.choice(randomLocatie)


    outfile = open('file.txt', 'a')    # naar txt file schrijven
    outfile.write(naam + ';' + bericht + ';' + locatie + ';' + dateTime + '\n')



def onclick():
    """
    word aangeroepen waanner er op de knop in gui word geklikt
    in een while loop zodat er op nieuw geprobeert kan worden wanneer het te lang is of ; in bericht

    """
    loop = True
    while loop == True:
        bericht = beoordeling.get("1.0", END)   # haalt het bericht uit gui

        if len(bericht) > 140 or ';' in bericht:  # checkt het bericht

            foutbericht = Label(master=root,   # wanneer bericht niet goed is
                                text='Dit bericht is te lang of heeft een ; probeer het opnieuw',
                                background='darkblue',
                                foreground='yellow',
                                font=('Ariel', 22, 'bold italic'))
            foutbericht.pack()
            loop = False
        else:   # bericht is goed dus word deze weg geschreven
            wegschrijven(bericht)
            loop = False
            beoordeling.delete('1.0','end') #leegt de text vakken voor de volgende reiziger
            naamtext.delete('1.0','end')



root = Tk()           #gui
root.title('Beoordeelprogrammatje')
root.geometry("800x400")
root.configure(bg='darkblue')
p1 = PhotoImage(file='NSicon.png')
root.iconphoto(False, p1)

label = Label(master=root,
                text='Laat hier je beoordeling achter!',
                background='darkblue',
                foreground='yellow',
                font=('Ariel', 25, 'bold italic'),
                pady=20)
label.pack()

beoordelingLabel = Label(master=root,
                             text='Vul hier je beoordeling in*',
                             background='darkblue',
                             foreground='white',
                             font=('Ariel', 12, 'bold italic'))
beoordelingLabel.pack()

beoordeling = Text(root, width=50, height=4, background='lightyellow', font=('Ariel', 12, 'bold italic'))
beoordeling.pack()

labelNaam = Label(master=root,
                  text='Vul hier je naam in',
                    background='darkblue',
                    foreground='white',
                    font=('Ariel', 12, 'bold italic'))
labelNaam.pack()

naamtext = Text(root, width=40, height=1, background='lightyellow', font=('Ariel', 12, 'bold italic'))
naamtext.pack()

button = Button(master=root, text='Klaar', background='Yellow', command=onclick)
button.pack(pady=(20, 10))

root.mainloop()












