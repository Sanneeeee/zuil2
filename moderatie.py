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

moderatie()