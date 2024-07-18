from helper import decoreer

def print_aanbieding ():
    prijzen = {
        "aardbei" : 3.0,
        "vanille" : 4.0,
        "chocolade" : 5.0
    } #2
    #3
    aanbieding = prijzen["vanille"] * 0.8
    #4
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
    reclame_tekst2 = reclame_tekst[:63] 
    #5 Niet van toepassing, want het probleem doet zich niet voor
    reclame_tekst3 = reclame_tekst.upper()
    #6
    reclame_tekst4 = reclame_tekst3.split(" ") #7
    for el in reclame_tekst4:
        if len(el) > 4: print(el.upper())
        else: print(el.lower())

decoreer("Aanbieding")
print_aanbieding()
        


   
