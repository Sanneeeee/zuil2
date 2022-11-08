from datetime import datetime#voor het krijgen van de datum en tijd
import psycopg2

def schrijvenDB(moderaterID,naam,bericht,locatie,datumTijd,dateTimeBeoordeling):
    """
    functie schrijft alle goedgekeurde berichten naar DB

    :param moderaterID: ID van de moderater
    :param naam: Naam van de reiziger
    :param bericht: bericht van de reiziger
    :param locatie: locatie van waar het bericht komt
    :param datumTijd: Datum en tijd van het bericht
    :param dateTimeBeoordeling:  datum en tijd van de moderatie
    :return:
    """

    connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Ez7kaieb'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    insert = """INSERT INTO beoordeling(Naam,Bericht,tijddatum,tijddatumkeuring,moderaterid,stationsnaam,beoordelingid)
                VALUES(%s,%s,%s,%s,%s,%s,DEFAULT)"""

    data = (naam, bericht, datumTijd, dateTimeBeoordeling, moderaterID, locatie)
    cursor.execute(insert, data)
    conn.commit()
    conn.close()

def moderatie():
    """
    moderater kan de berichten lezen en deze goed of afkeuren
    :return:
    """
    moderater = input('voer eerst je moderaterID in:') #Elke moderater heeft een ID gekregen
    moderaterID = int(moderater)

    outfile = open('file.txt', 'r') #opent txt file om alle regels hier uit telezen
    regels = outfile.readlines()

    for regel in regels: #gaat langs elke regel in de txt file
        berichtInfo = regel.split(';') #split list op de ;'s zo dat je alle info los van elkaar hebt
        naam = berichtInfo[0]
        bericht = berichtInfo[1]
        locatie = berichtInfo[2]
        datumTijd = berichtInfo[3].strip('\n')

        now = datetime.now()   #datum en tijd van moment van moderatie
        dateTimeBeoordeling = now.strftime("%d/%m/%Y %H:%M:%S")

        print(bericht)
        print(naam)
        beoordeling = input('typ g voor goedkeuring f voor afkeuring: ')


        if beoordeling == 'g' or beoordeling == '':   #als is goedgekeurd word de functie aangeroepen om het naar DB te schrijven
            print('Goedgekeurd')
            # moet worden door geschreven naar db
            # mag worden weergegeven op stations bord
            schrijvenDB(moderaterID,naam,bericht,locatie,datumTijd,dateTimeBeoordeling)

        elif beoordeling == 'f':
            print('Afgekeurd')

        else:
            print('deze waarde kunnen we niet herkennen.')

    outfile.close()


    outfile = open('file.txt', 'w') #File geleegt na moderatie
    outfile.close()

moderatie() # aanroepen moderatie