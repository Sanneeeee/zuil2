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

def moderatie():
    outfile = open('file.txt', 'r')
    regels = outfile.readlines()
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
            print('.')#moet worden door geschreven naar db
            # mag worden weergegeven op stations bord
        elif beoordeling == 'fout':
            print('@') #moet worden door geschreven naar db
             # mag niet worden weergegeven op stations bord
        else:
            print('deze waarde kunnen we niet aan nemen')


loop = True
while loop == True:
    moderatie()
    print('Je bericht mag net langer zijn dan 140 karakters!')
    bericht = input('Geef ons je mening:')

    if len(bericht) <= 140:
        wegschrijven()
        loop = False
    else:
        print('Dit bericht is te lang probeer het opnieuw')





