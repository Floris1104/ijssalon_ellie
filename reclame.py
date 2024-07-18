from algemene_functies import mijn_functie_1 #werkt
from algemene_functies import mijn_functie_2 #werkt

def aanbieding_1(smaak, prijs, korting): #werkt
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs*korting} euro."

def inkomsten_totaal(inkomsten, btw): #werkt
    return f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {btw*sum(inkomsten)} euro btw betaald dient te worden."

def hoog_en_laag(mijn_lijst): #werkt
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst): #werkt
    return f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst)/len(mijn_lijst)} euro."

def meervoudig(invoer_lijst): #werkt
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2): 
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])
   


 
