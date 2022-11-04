from tkinter import *
import requests
import json


def stationscherm(stationnaam,lat,lon):
    Weer = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=nl&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
    omschrijving = json.loads(Weer.text)['weather']
    temp = json.loads(Weer.text)['main']
    print(omschrijving[0]['description'])
    print(temp['temp'],'Celcius')

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
              font=('Ariel', 25, 'bold italic'))
    label.grid(row=0, column = 0, padx=10, pady=10)


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


