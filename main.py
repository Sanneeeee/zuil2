import random
import requests
import json
import psycopg2
from datetime import datetime#voor het krijgen van de datum en tijd
from tkinter import *


def wegschrijven(bericht):
    """
    :return:
    """
    naamNewLine = naamtext.get("1.0", END)

    naamlst=naamNewLine.split('\n')    #haalt de \n erachter weg
    naam = naamlst[0]
    berichtlst=bericht.split('\n')
    bericht = berichtlst[0]
    # lst=[naam,bericht]
    # print(lst)


    if naam == '' or naam == '.' or naam == ' ':
        naam = 'anoniem'

    now = datetime.now()
    dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    #print(dateTime)

    randomLocatie = ['Utrecht', 'Assen', 'Zwolle', 'Groningen']
    locatie = random.choice(randomLocatie)
    #print(locatie)

    outfile = open('file.txt', 'a')
    outfile.write(naam + ';' + bericht + ';' + locatie + ';' + dateTime + '\n')
    #print('Bedankt voor je beoordeling!')



def onclick():
    loop = True
    while loop == True:
         #moderatie()
        # print('Je bericht mag niet langer zijn dan 140 karakters!')
        # bericht = input('Geef ons je mening:')

        bericht = beoordeling.get("1.0", END)

        if len(bericht) > 140 or ';' in bericht:
            # print('Dit bericht is te lang of heeft een ; probeer het opnieuw')
            foutbericht = Label(master=root,
                                text='Dit bericht is te lang of heeft een ; probeer het opnieuw',
                                background='darkblue',
                                foreground='yellow',
                                font=('Ariel', 22, 'bold italic'))
            foutbericht.pack()
            loop = False
        else:
            wegschrijven(bericht)
            loop = False
            beoordeling.delete('1.0','end')
            naamtext.delete('1.0','end')



root = Tk()
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
    # print(a.get("1.0", END))
beoordeling.pack()

labelNaam = Label(master=root,
                  text='Vul hier je naam in',
                    background='darkblue',
                    foreground='white',
                    font=('Ariel', 12, 'bold italic'))
labelNaam.pack()

naamtext = Text(root, width=40, height=1, background='lightyellow', font=('Ariel', 12, 'bold italic'))
    # print(a.get("1.0", END))
naamtext.pack()

button = Button(master=root, text='Klaar', background='Yellow', command=onclick)
button.pack(pady=(20, 10))

root.mainloop()












