import random
from datetime import datetime  #voor het krijgen van de datum en tijd
def wegschrijven():
    naam = input('Vul je naam in:')

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

loop = True
while loop == True:

    print('Je bericht mag net langer zijn dan 140 karakters!')
    bericht = input('Geef ons je mening:')

    if len(bericht) <= 140:
        wegschrijven()
        loop = False
    else:
        print('Dit bericht is te lang probeer het opnieuw')