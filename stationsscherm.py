from tkinter import *
import requests
import json
import psycopg2

from PIL import Image, ImageTk

#def beoordelingen():




def stationscherm(stationnaam,lat,lon):
    Weer = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=nl&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
    omschrijving = json.loads(Weer.text)['weather']
    temp = json.loads(Weer.text)['main']
    print(omschrijving[0]['description'])
    print(temp['temp'],'C')

    root = Tk()
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

    image = Image.open("NS-white.png")
    resize_image = image.resize((150, 64))

    img = ImageTk.PhotoImage(resize_image)
    label = Label(image=img,
                  background='darkblue')
    label.image = img  # keep a reference!
    label.grid(sticky="W", row=0, column=1)

    label = Label(master=root,
                  text=f'{omschrijving[0]["description"]}\n{round(temp["temp"])} °C',
                  background='darkblue',
                  foreground='white',
                  font=('Ariel', 25, 'bold italic'))
    label.grid(sticky="W", row=0, column=2)


    img = ImageTk.PhotoImage(resize_image)
    label = Label(image=img,
                  background='darkblue')
    label.image = img  # keep a reference!
    label.grid(sticky="E", row=0, column=1)





    i=0
    for m in ('Naam', 'Bericht', '  Datum & Tijd  ', 'Station'):

        label = Label(master=root,
                    text=m,
                    background='lightblue',
                    foreground='black',
                    font=('Ariel', 23, 'bold italic'),
                    width = 12)
        label.grid(row=1, column=i, padx=0, pady=10)
        i+=1

    label = Label(master=root,
                  text='Facaliteiten',
                  background='lightblue',
                  foreground='black',
                  font=('Ariel', 23, 'bold italic'),
                  width=12)
    label.grid(row=1, column=4, columnspan=4, padx=0, pady=10)


    connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"
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
    for record in records:
        print(record)
        print(len(record[1]))
        p = 0
        c = 0
        for item in record:
            if item == record[4] or item == record[5] or item == record[6] or item == record[7]:
                p+=1

                if item == True and p == 1:
                    faciliteit = 'ovfiets'
                    c += 1
                elif item == True and p == 2:
                    faciliteit = 'lift'
                    c += 1
                elif item == True and p == 3:
                    print(3)
                    faciliteit = 'toilet'
                    c += 1
                elif item == True and p == 4:
                    print(4)
                    faciliteit = 'pr'
                    c+=1

                if faciliteit != '':
                    image = Image.open(f"img_{faciliteit}.png")
                    resize_image = image.resize((75, 64))

                    img = ImageTk.PhotoImage(resize_image)
                    label = Label(image=img)
                    label.image = img  # keep a reference!
                    label.grid(row=n, column=c, pady=5, padx=10)
                    faciliteit = ''
                # c += 1



            else:
                label = Label(master=root,
                            text=f'{item}',
                            background='darkblue',
                            foreground='yellow',
                            font=('Ariel', 18, 'bold italic'))
                label.grid(row=n, column=c, padx=0, pady=10)
                c+=1

        n+=1







    root.mainloop()

station = input('Vul hier in van welk station je het stationsscherm wilt openen: ')

if station == 'Zwolle' or station == 'Utrecht' or station == 'Assen':
    if station == 'Zwolle':
         lat = '52.5055809'
         lon = '6.0905981'

    elif station == 'Utrecht':
        lat = '52.096255'
        lon = '5.111773'
    else:
        lat = '52.9927884'
        lon = '6.5697139'

    stationscherm(station,lat,lon)
else:
    print('Dit station bestaat niet!')


