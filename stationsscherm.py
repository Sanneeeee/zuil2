from tkinter import *
import requests
import json

#api ofz
#x = requests.get('https://www.omdbapi.com/?i=tt3896198&apikey=1d9ee833&t=witness&y=2021')

#print(json.loads(x.text)['Title'])

#assen
#Breedtegraad (latitude): 52.9927884
#Lengtegraad (longitude): 6.5697139

#zwolle station	lat=52.5055809	lon=6.0905981

#Utrecht centraal station	lat=52.096255	lon=5.111773
#x = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b3bd55f1b2628390c9ead2b6f1972f2d')
WeerAssen = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=52.9927884&lon=6.5697139&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
print(json.loads(WeerAssen.text))

WeerZwolle = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=52.5055809&lon=6.0905981&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
print(json.loads(WeerZwolle.text))

WeerUtrecht = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=52.096255&lon=5.111773&appid=b3bd55f1b2628390c9ead2b6f1972f2d')
print(json.loads(WeerUtrecht.text))



def stationscherm():
    root = Tk()
    root.title('Stationsschermpje')
    root.geometry("800x400")
    root.configure(bg='darkblue')
    p1 = PhotoImage(file='NSicon.png')
    root.iconphoto(False, p1)
    root.mainloop()

#station = input('Vul hier in van welk station je het stationsscherm wilt openen: ')



