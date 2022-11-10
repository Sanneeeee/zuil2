from tkinter import *
import requests
import json
import psycopg2
from PIL import Image, ImageTk
from urllib.request import urlopen


def stationscherm(stationnaam,lat,lon):
    """
    Functie maakt het stations scherm met info van DB en van Openweather

    :param stationnaam: De naam van het station
    :param lat: lengtegraad van het station
    :param lon: breedtegraad van het station

    """
    #info opgevraagd van locatie door het mee geven van lat en lon
    Weer = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=nl&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
    omschrijving = json.loads(Weer.text)['weather']
    temp = json.loads(Weer.text)['main']

    root = Tk() #start gui
    root.title('Stationsschermpje')
    root.geometry("800x400")
    root.configure(bg='darkblue')
    p1 = PhotoImage(file='NSicon.png')
    root.iconphoto(False, p1)

    label = Label(master = root,
              text = f'{stationnaam}',
              background = 'darkblue',
              foreground= 'white',
              font=('Ariel', 40, 'bold italic'))
    label.grid(row=0, column = 0, padx=10, pady=10)

    icon = f'https://openweathermap.org/img/wn/{omschrijving[0]["icon"]}@2x.png'
    u = urlopen(icon)
    raw_data = u.read()
    u.close()

    photo = ImageTk.PhotoImage(data=raw_data)

    label = Label(image=photo,  # het weer icon
                  background='darkblue')

    label.grid(sticky="E", row=0, column=1)

    label = Label(master=root,   # weer omschrijving plus de Temp
                  text=f'{omschrijving[0]["description"]}\n{round(temp["temp"])} °C',
                  background='darkblue',
                  foreground='white',
                  font=('Ariel', 25, 'bold italic'))
    label.grid(sticky="W", row=0, column=2)

    image = Image.open("NS-white.png") # Ns logo
    resize_image = image.resize((150, 64))
    img = ImageTk.PhotoImage(resize_image)
    label = Label(image=img,
                   background='darkblue')
    label.image = img  # keep a reference!
    label.grid(sticky="W", row=0, column=1)


    i=0
    for m in ('Naam', 'Bericht', '  Datum & Tijd  ', 'Station'):  #aanmaken van de namen van de kolommen

        label = Label(master=root,
                    text=m,
                    background='lightblue',
                    foreground='black',
                    font=('Ariel', 23, 'bold italic'),
                    width = 12)
        label.grid(row=1, column=i, padx=0, pady=10, sticky='WE')
        i+=1

    label = Label(master=root,
                  text='Facaliteiten',
                  background='lightblue',
                  foreground='black',
                  font=('Ariel', 23, 'bold italic'),
                  width=12)
    label.grid(row=1, column=4, columnspan=4, padx=0, pady=10, sticky ='WE')


    connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"  #connectie maken met DB om hier gegeven uit te halen
    conn = psycopg2.connect(connection_string)  # get a connection with the database
    cursor = conn.cursor()  # a ‘cursor’ allows to execute SQL in a db-session
    query = """SELECT naam, bericht, tijddatum, Beoordeling.stationsnaam, stationfaciliteiten.ovfiets, stationfaciliteiten.lift, stationfaciliteiten.wc, stationfaciliteiten.pr
                from Beoordeling
                INNER JOIN Stationfaciliteiten ON Beoordeling.stationsnaam = stationfaciliteiten.stationsnaam
                order by "beoordelingid" DESC LIMIT 5;"""  # the string
    cursor.execute(query)
    records = cursor.fetchall()  # retrieve the records from the database
    conn.close()


    n = 2
    for record in records: #gaat elke row met data bij langs

        p = 0
        c = 0
        for item in record: #gaat elk item in deze rij bij langs
            if item == record[4] or item == record[5] or item == record[6] or item == record[7]: #checkt of het om een item gaaat die als icon word weergegeven
                p+=1

                if item == True and p == 1:
                    faciliteit = 'ovfiets'
                    c += 1
                elif item == True and p == 2:
                    faciliteit = 'lift'
                    c += 1
                elif item == True and p == 3:
                    faciliteit = 'toilet'
                    c += 1
                elif item == True and p == 4:
                    faciliteit = 'pr'
                    c+=1

                if faciliteit != '': # maakt de icon
                    image = Image.open(f"img_{faciliteit}.png")
                    resize_image = image.resize((75, 64))

                    img = ImageTk.PhotoImage(resize_image)
                    label = Label(image=img)
                    label.image = img  # keep a reference!
                    label.grid(row=n, column=c, pady=5, padx=5)
                    faciliteit = ''
                # c += 1



            else:
                label = Label(master=root, # zet de item in het schema
                            text=f'{item}',
                            background='darkblue',
                            foreground='yellow',
                            font=('Ariel', 18, 'bold italic'),
                            width=0,
                            wraplength=500)
                label.grid(row=n, column=c, padx=0, pady=10)
                c+=1

        n+=1

    root.mainloop()

station = input('Vul hier in van welk station je het stationsscherm wilt openen: ')

if station == 'Zwolle' or station == 'Utrecht' or station == 'Assen': # checkt of ingevulde naam juist is en geeft vervaling de lat en lon hiervoor mee
    if station == 'Zwolle':
         lat = '52.5055809'
         lon = '6.0905981'

    elif station == 'Utrecht':
        lat = '52.096255'
        lon = '5.111773'
    else:
        lat = '52.9927884'
        lon = '6.5697139'

    stationscherm(station,lat,lon) #aanroepen scherm functie
else:
    print('Dit station bestaat niet!')


