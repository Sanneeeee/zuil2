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
    naam = naamtext.get("1.0", END)

    if naam == '' or naam == '.' or naam == ' ':
        naam = 'anoniem'

    now = datetime.now()
    dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    #print(dateTime)

    randomLocatie = ['Utrecht', 'Emmen', 'Zwolle']
    locatie = random.choice(randomLocatie)
    #print(locatie)

    outfile = open('file.txt', 'a')
    outfile.write(naam + ';' + bericht + ';' + locatie + ';' + dateTime + '\n')
    print('Bedankt voor je beoordeling!')

def onclick():
    loop = True
    while loop == True:
         #moderatie()
        # print('Je bericht mag niet langer zijn dan 140 karakters!')
        # bericht = input('Geef ons je mening:')

        bericht = beoordeling.get("1.0", END)

        if len(bericht) <= 140 or ';' in bericht:
            wegschrijven(bericht)
            loop = False
        else:
            print('Dit bericht is te lang of heeft een ; probeer het opnieuw')



def stationsScherm(regel, schermlijst):
    """

    :param regel:
    :param schermlijst:
    :return:
    """
    while len(schermLijst) < 5:
        schermLijst.append(regel)

    schermlist.pop(0)
    schermLijst.append(regel)
    return schermlijst


    #delete laatste en voeg een nieuwe toe


def moderatie():
    outfile = open('file.txt', 'r')
    regels = outfile.readlines()
    schermLijst = []
    for regel in regels:
        berichtInfo = regel.split(';')
        print(berichtInfo)
        naam = berichtInfo[0]
        bericht = berichtInfo[1]
        #locatie = berichtInfo[2]
        #datumTijd = berichtInfo[3].strip('\n')

        print(bericht)
        print(naam)
        beoordeling = input('typ goed voor goedkeuring fout voor afkeuring: ')


        if beoordeling == 'goed':
            print('.')
            # moet worden door geschreven naar db
            # mag worden weergegeven op stations bord
            schermLijst = stationsScherm(regel, schermLijst)
            print(stationsScherm())
        elif beoordeling == 'fout':
            print('@')

        else:
            print('deze waarde kunnen we niet herkennen.')


#x = requests.get('https://www.omdbapi.com/?i=tt3896198&apikey=1d9ee833&t=witness&y=2021')

#print(json.loads(x.text)['Title'])

#connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"
#conn = psycopg2.connect(connection_string)  # get a connection with the database
#cursor = conn.cursor()

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



beoordeling = Text(root, width=50, height=4,background='lightyellow',font=('Ariel', 12, 'bold italic'))
#print(a.get("1.0", END))
beoordeling.pack()

labelNaam = Label(master=root,
              text='Vul hier je naam in',
              background='darkblue',
              foreground='white',
              font=('Ariel', 12, 'bold italic'))
labelNaam.pack()

naamtext = Text(root, width=40, height=1,background='lightyellow')
#print(a.get("1.0", END))
naamtext.pack()

button = Button(master=root,text='Klaar',background='Yellow', command = onclick)
button.pack(pady=(20,10))


root.mainloop()










