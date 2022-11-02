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

    randomLocatie = ['Utrecht', 'Emmen', 'Zwolle']
    locatie = random.choice(randomLocatie)
    #print(locatie)

    outfile = open('file.txt', 'a')
    outfile.write(naam + ';' + bericht + ';' + locatie + ';' + dateTime + '\n')
    #print('Bedankt voor je beoordeling!')
    bedanktbericht = Label(master=root,
                      text='Bedankt voor je beoordeling!',
                      background='darkblue',
                      foreground='yellow',
                      font=('Ariel', 22, 'bold italic'))
    bedanktbericht.pack()

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

def schrijvenDB(moderaterID,naam,bericht,locatie,datumTijd,dateTimeBeoordeling):

    connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    insert = """INSERT INTO beoordeling(Naam,Bericht,tijddatum,tijddatumkeuring,moderaterid,stationsnaam,beoordelingid)
                VALUES(%s,%s,%s,%s,%s,%s,DEFAULT)"""

    data = (naam, bericht, datumTijd, dateTimeBeoordeling, moderaterID, locatie)
    cursor.execute(insert, data)
    #records = cursor.fetchall()
    conn.commit()
    conn.close()

def moderatie():
    moderater = input('voer eerst je moderaterID in:')
    moderaterID = int(moderater)

    outfile = open('file.txt', 'r')
    regels = outfile.readlines()

    for regel in regels:
        berichtInfo = regel.split(';')
        print(berichtInfo)
        naam = berichtInfo[0]
        bericht = berichtInfo[1]
        locatie = berichtInfo[2]
        datumTijd = berichtInfo[3].strip('\n')

        now = datetime.now()
        dateTimeBeoordeling = now.strftime("%d/%m/%Y %H:%M:%S")

        print(bericht)
        print(naam)
        beoordeling = input('typ g voor goedkeuring f voor afkeuring: ')


        if beoordeling == 'g' or beoordeling == '':
            print('.')
            # moet worden door geschreven naar db
            # mag worden weergegeven op stations bord
            schrijvenDB(moderaterID,naam,bericht,locatie,datumTijd,dateTimeBeoordeling)

        elif beoordeling == 'f':
            print('@')

        else:
            print('deze waarde kunnen we niet herkennen.')

    outfile.close()


    outfile = open('file.txt', 'w')
    outfile.close()

#api ofz
#x = requests.get('https://www.omdbapi.com/?i=tt3896198&apikey=1d9ee833&t=witness&y=2021')

#print(json.loads(x.text)['Title'])

#connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"
#conn = psycopg2.connect(connection_string)  # get a connection with the database
#cursor = conn.cursor()%

moderatie()

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










