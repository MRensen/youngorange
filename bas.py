#start dorp > Moeras, boerderij, Strand
#Moeras > bos > kerkhof
#boerderij > Bos , Kerkhof
#strand > Bos, schipwrak
#kerkhof > Vijand zombie, hoger rollen dan 6 > taverne
#Bos > Vijand wolf, hoger rollen dan 3 > taverne
#Schipwrak > vijand grote krab, hoger rollen dan 4 > taverne
from typing import final

keep_going = True
while keep_going:
    print("Je avondtuur begint! waar ga je heen?")
    keuze = input("moeras, boerderij, strand ").lower()
    while not (keuze == "moeras" or keuze == 'boerderij' or keuze == "strand"):
        print("je raakt verdwaald, game over")
        break
    #Moeras
    if keuze == "moeras":
        print("je komt aan in het natte Moeras, in de verte zie je het kerkhof ")
        keuze2 =input("Ga je verder naar het Kerkhof(gevaar!) of naar het  bos(veilig) ernaast?").lower()
        while not (keuze2 == "kerkhof" or keuze2 == "bos"):
            keuze2 = input("deze keuze is niet mogelijk, Ga je verder naar het Kerkhof(gevaar!) of naar het  bos(veilig) ernaast?").lower()

        #kerkhof
        if keuze2 == "kerkhof":
            print("je komt aan in het enge kerkhof, uit de grond komt een zombie! val je aan of ren je weg?")
            gevecht = input("vechten, vluchten").lower()
            while not (gevecht == "vechten" or gevecht == "vluchten"):
                print("Helaas! je hebt maar twee keuzes, Aanvallen of Vluchten").lower()
            if gevecht == "vechten":
                import random
                aanval = random.randint(1, 7)
                print(aanval)
                if aanval >= 5:
                    print("De zombie is verslagen!")

                    bier = True
                else:
                    print("Helaas, De zombie heeft je gebeten, Game over!")
                    keep_going = False
                    # gevecht vluchten
            elif gevecht == "vluchten":
                    print("Je bent terug gevlucht naar het dorp. Probeer het nog eens")
        #bos
        elif keuze2 == "bos":
            print("je loopt door het vredige bos, plots word je besprongen door een wolf!")
            gevecht = input (" vechten of vluchten? ")
            if gevecht == "vechten":
                import random

                aanval = random.randint(1, 7)
                print(aanval)
                if aanval >= 2:

                    print("wow! je hebt de wolf verslagen")
                    #bier
                    bier=True
                else:
                    print("Helaas, de wolf heeft je verscheurd, game over!")
     # gevecht vluchten
            elif gevecht == "vluchten":
                print("Je bent terug gevlucht naar het dorp. spel over")
    #boerderij

    elif keuze == "boerderij":
        print("je loopt door een kalmerend weiland, je komt aan bij de rand van het bos, echt zie je ook "
              "het pad righting het kerkhof")
        keuze2 = input("ga je het bos in of neem je het pad naar het kerkhof?")

        #bos
        if keuze2 == "bos":
            print("je loopt door het vredige bos, plots word je besprongen door een wolf!")
            gevecht = input (" vechten of vluchten? ")
            if gevecht == "vechten":
                import random

                aanval = random.randint(1, 7)
                print(aanval)
                if aanval >= 2:
                    print("wow! je hebt de wolf verslagen")
                    bier=True
                else:

                   print("Helaas, de wolf heeft je verscheurd, game over!")
            #gevecht vluchten
            elif gevecht == "vluchten":
                print("Je bent terug gevlucht naar het dorp. spel over")
        #kerkhof
        elif keuze2 == "kerkhof":
            print("je komt aan in het enge kerkhof, uit de grond komt een zombie! val je aan of ren je weg?")
            gevecht = input("vechten, vluchten").lower()
            while not (gevecht == "vechten" or gevecht == "vluchten"):
                print("Helaas! je hebt maar twee keuzes, Aanvallen of Vluchten").lower()
            if gevecht == "vechten":
                import random

                aanval = random.randint(1, 7)
                print(aanval)
                if aanval >= 5:
                    print("De zombie is verslagen!")

                    # bier!
                    bier=True

                else:
                    print("Helaas, De zombie heeft je gebeten, Game over!")
                    # gevecht vluchten
            elif gevecht == "vluchten":
                print("Je bent terug gevlucht naar het dorp. spel over")

    #strand

    elif keuze == "strand":
        print("je komt aan op een prachtig strand, bij het water zie je een schipwrak"
              "maar je ziet in de duinen ook een pad naar het bos")
        keuze2 = input("Loop je naar het schipwrak of ga je het bos in")

        #schipwrak
        if keuze2 == "schipwrak":
            print("je loopt over het krakende hout van het schip, plots springt er een grote krab "
                  "uit het water!")
            gevecht = input("vechten of vluchten")
            if gevecht == "vechten":
                import random

                aanval = random.randint(1, 7)
                print(aanval)
                if aanval >= 5:
                    print("de krab valt dood neer!")
                    # bier!
                    bier=True
                else:
                    print("helaas, de krab heeft je dood geknepen, game over")
            # bos
        elif keuze2 == "bos":
                print("je loopt door het vredige bos, plots word je besprongen door een wolf!")
                gevecht = input(" vechten of vluchten? ")
                if gevecht == "vechten":
                    import random

                    aanval = random.randint(1, 7)
                    print(aanval)
                    if aanval >= 2:

                        print("wow! je hebt de wolf verslagen")
                        # bier
                        bier = True
                    else:
                        print("Helaas, de wolf heeft je verscheurd, game over!")
                # gevecht vluchten
                elif gevecht == "vluchten":
                    print("Je bent terug gevlucht naar het dorp. spel over")
# Niveau 1
if moeras:
    pass
if boerderij:
    pass
if strad:
    pass

#niveau 2
if kerkhof:
    pass
if bos:
    pass
if strand:

# niveau 3
if bier:
    # bier!
    bier = input("wil je dit vieren in de taverne met bier? schreeuw maar bier!")
    if bier == "bier":
        print("je drinkt bier in overloed in de tarverne, spel compleet")
    while not (bier == "ja" or bier == "bier" or bier == "bier!!"):
        bier = input("Hoor ik bier??")

if verslagen:
    pass

