print("Dodawania filmow")

ilosc_filmow = int(input("Podaj ile chcesz dodac filmow na serwer?: "))

calkowita_wielkosc_filmow = 0
maksymalna_pojemnosc_slotu = 10000
ilosc_slotow = 1
zajete_miejsce_aktualnego_slotu = 0
slot_z_najmniejszym_zajetym_miejscem = 1
najlezejszy_slot = 10000

for numer_filmow in range(ilosc_filmow):
    rozmiar_filmow = float(input(f"Poda rozmiar filmu {numer_filmow + 1}(w MB): "))
    if rozmiar_filmow < 10 or rozmiar_filmow > 3000:
        break
    calkowita_wielkosc_filmow += rozmiar_filmow
    if zajete_miejsce_aktualnego_slotu + rozmiar_filmow > maksymalna_pojemnosc_slotu:
        if zajete_miejsce_aktualnego_slotu < najlezejszy_slot:
            najlezejszy_slot = zajete_miejsce_aktualnego_slotu
            slot_z_najmniejszym_zajetym_miejscem = ilosc_slotow
        ilosc_slotow += 1
        zajete_miejsce_aktualnego_slotu = 0
    zajete_miejsce_aktualnego_slotu += rozmiar_filmow
if calkowita_wielkosc_filmow == 0:
    ilosc_slotow = 0
    print("Nie dodales zadnego filmu")
else:
    print(f"Calkowita rozmiar wszystkich fulmow {calkowita_wielkosc_filmow} Mb")
    print(f"Ilosc slotów: {ilosc_slotow}")
    print(
        f"Ilosc pustej przestszeni: {ilosc_slotow * maksymalna_pojemnosc_slotu - calkowita_wielkosc_filmow}"
    )
    print(
        f"Najlzejszy slot to {slot_z_najmniejszym_zajetym_miejscem}, mial {maksymalna_pojemnosc_slotu - najlezejszy_slot} wolnego miejsca"
    )
