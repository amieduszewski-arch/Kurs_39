print("PostIn Wita!")

ilosc_elementow = int(input("Podaj ile elementow chcesz wyslac?: "))

paczka = 1
waga_paczki = 0
suma_wagi = 0
najwiecej_pustych = 0
nr_paczki_max_puste = 1
ilosc_paczek = 0

for i in range(ilosc_elementow):
    waga_elementu = float(input(f"Podaj wage elementu nr {i+1}: "))

    if waga_elementu < 1 or waga_elementu > 10:
        print("Waga poza zakresem 1–10 kg, koniec pakowania")
        break

    if waga_paczki + waga_elementu > 20:
        ilosc_paczek += 1
        puste = 20 - waga_paczki
        if puste > najwiecej_pustych:
            najwiecej_pustych = puste
            nr_paczki_max_puste = ilosc_paczek
        print(f"Paczka {ilosc_paczek} wyslana z waga {waga_paczki} kg")
        suma_wagi += waga_paczki
        waga_paczki = 0
        paczka += 1

    waga_paczki += waga_elementu

if waga_paczki > 0:
    ilosc_paczek += 1
    puste = 20 - waga_paczki
    if puste > najwiecej_pustych:
        najwiecej_pustych = puste
        nr_paczki_max_puste = ilosc_paczek
    print(f"Paczka {ilosc_paczek} wyslana z waga {waga_paczki} kg.")
    suma_wagi += waga_paczki

suma_pustych = ilosc_paczek * 20 - suma_wagi

print("\n PODSUMOWANIE")
print(f"Wyslano {ilosc_paczek} paczek")
print(f"Wyslano {suma_wagi} kg towaru")
print(f"Suma pustych kilogramow: {suma_pustych} kg.")
print(f"Najwiecej pustych kilogramow ma paczka {nr_paczki_max_puste} ({najwiecej_pustych} kg).")