gain = 1.0
pi = 3.14

def prameter_abfrage():
    print("Gebe nötige Werte an:")
    breite = float(input("Leinwand-Breite (in cm) -> "))
    hoehe = float(input("Leinwand-Höhe (in cm) -> "))
    lumen = float(input("Projektor-Lumen -> "))
    return breite, hoehe, lumen

def flaeche_berechnung(breite, hoehe):
    flaeche_meter = (breite/100) * (hoehe/100)
    return flaeche_meter

def lux_berechnung(lumen, flaeche):
    return lumen / flaeche

def nits_berechnung(lux, gain, pi):
    nits = (lux * gain) / pi
    return round(nits)

while True:
    ausfuehren = True
    while ausfuehren:
        b, h, l = prameter_abfrage()
        f = flaeche_berechnung(b, h)
        lux_wert = lux_berechnung(l, f)
        nits_ergebnis = nits_berechnung(lux_wert, gain, pi)

        print(f"Helligkeit in Nits: {nits_ergebnis} nits")
        abfrage = input("Beenden? J/N -> ").lower()

        if abfrage == "n" or abfrage == "nein":
            print(" ")
            ausfuehren = True
        else:
            ausfuehren = False
            print("Programm beendet")
            break
    break