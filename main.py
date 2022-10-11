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

def stationsScherm(regel, schermlijst):

    while len(schermLijst) < 5:
        schermLijst.append(regel)

    schermlijst.pop(0)
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
            #moet worden door geschreven naar db
             # mag niet worden weergegeven op stations bord
        else:
            print('deze waarde kunnen we niet herkennen.')



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





