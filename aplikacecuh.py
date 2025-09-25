vybava = []
zakaznici = []

def pridat_vybaveni():
    kategorie = input("Zadej kategorii: ")
    nazev = input("Zadej nazev: ")
    try:
        cena = int(input("Zadej pujcovaci cenu na den: "))
    except ValueError:
        print("Cislo bro")
        return
    vybava.append({
        "kategorie": kategorie,
        "nazev": nazev,
        "cena": cena,
        "dostupnost": True,
        "pocet_pujceni": 0
    })
    print(f"\nVybaveni pridano! {kategorie}, {nazev}")

def vypsat_vybaveni():
    if not vybava:
        print("Neni nic evidovano")
        return
    print("Seznam vybaveni: \n")
    for i in range(len(vybava)):
        item = vybava[i]
        print(f"{i+1}. {item['kategorie']}, {item['nazev']}, {item['cena']} Kc/Den, {item['dostupnost']} ")

def registrace_zakaznika():
    jmeno = input("Zadejte svoje jmeno: ")
    prijmeni = input("Zadejte svoje prijmeni: ")
    zakaznici.append({
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "vypujcka": []
    })
    print(f"\nZakaznik {jmeno} {prijmeni} registrovan")

def vypsat_zakazniky():
    if not zakaznici:
        print("Zadny zakaznik neni evidovan")
        return
    print("Seznam zakazniku: \n")
    for i in range(len(zakaznici)):
        zakaznik = zakaznici[i]
        print(f"{i+1}. {zakaznik['jmeno']}, {zakaznik['prijmeni']}, Pujceno {len(zakaznik['vypujcka'])}")

def pujcit_vybaveni():
    vypsat_zakazniky()
    if not zakaznici:
        return
    try:
        id_zak = int(input("Zadej ID zakaznika: ")) - 1
        if id_zak < 0 or id_zak >= len(zakaznici):
            print("Neplatne ID zakaznika")
            return
    except ValueError:
        print("Chyba clovece, tento uzivatel je neplatny")
        return

    vypsat_vybaveni()
    try:
        id_vyb = int(input("Zadejte ID vybaveni: ")) - 1
        if id_vyb < 0 or id_vyb >= len(vybava):
            print("ID neexistuje.")
            return
    except ValueError:
        print("Neplatny vstup")
        return

    vyb = vybava[id_vyb]
    if not vyb["dostupnost"]:
        print("Polozka neni volna")
        return

    vyb["dostupnost"] = False
    vyb["pocet_pujceni"] += 1
    zakaznici[id_zak]["vypujcka"].append(id_vyb)
    print(f"Vybaveni: '{vyb['nazev']}' vypujcil {zakaznici[id_zak]['jmeno']} {zakaznici[id_zak]['prijmeni']}")
    print(f"Cena za den: {vyb['cena']} Kc")

def zobrazit_statistiku():
    celkem = len(vybava)
    dostupne = sum(1 for v in vybava if v["dostupnost"])
    print("\nStatistika:")
    print(f"Pocet pujcenych polozek: {celkem}")
    print(f"Dostupne polozky: {dostupne}")
    print(f"Pocet zakazniku: {len(zakaznici)}")

def menu():
    while True:
        print("\nAplikacni Menu")
        print("1 - Pridat vybaveni")
        print("2 - Vypsat vybaveni")
        print("3 - Zaregistrovat se")
        print("4 - Vypsat zakazniky")
        print("5 - Pujcit vybaveni ")
        print("6 - Statistika")
        print("0 - Konec")
        volba = input("Zadej volbu: ").strip()

        if volba == "1":
            pridat_vybaveni()
        elif volba == "2":
            vypsat_vybaveni()
        elif volba == "3":
            registrace_zakaznika()
        elif volba == "4":
            vypsat_zakazniky()
        elif volba == "5":
            pujcit_vybaveni()
        elif volba == "6":
            zobrazit_statistiku()
        elif volba == "0":
            print("Konec")
            break
        else:
            print("Volba neexistuje")

menu()