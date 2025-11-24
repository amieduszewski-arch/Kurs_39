salo_sklepu = 50000.0
zbor_produktow = [
    {
        "Nazwa_produktu": "iPhone 15 pro",
        "Rok_Produkcji": "2023",
        "Cena": "4999.99",
        "Ilosc": 3,
        "ASIN": "23"
     },
    {
        "Nazwa_produktu": "iPhone 16 pro",
        "Rok_Produkcji": "2024",
        "Cena": "5299.99",
        "Ilosc": 2,
        "ASIN": "2323"
     },
    {
        "Nazwa_produktu": "iPhone 17 pro",
        "Rok_Produkcji": "2025",
        "Cena": "5999.99",
        "Ilosc": 2,
        "ASIN": "232323"
    }
]

historia_operacji = []

while True:
    wybor = input("""
Wybierz jedną z poniższych komend:
1. saldo
2. sprzedaż
3. zakup
4. konto
5. lista
6. magazyn
7. przegląd
8. koniec
Podaj numer komendy: """)
    match wybor:
        case "1":
            srodki = float(input("Podaj kwotę do doładowania (lub ujemną do odjęcia): "))
            if salo_sklepu + srodki < 0:
                print("Nie możesz ustawić salda na wartość ujemną.")
            else:
                salo_sklepu += srodki
                historia_operacji.append(f"saldo: {srodki}")
                print(f"Aktualne saldo wynosi: {salo_sklepu} PLN")
        case "2":
            numer_asin = input("Podaj numer ASIN produktu do sprzedaży: ")
            znaleziono_produkt = False
            for produkt in zbor_produktow:
                if produkt.get("ASIN") == numer_asin:
                    znaleziono_produkt = True
                    ilosc = int(input("Podaj liczbę sztuk do sprzedaży: "))
                    if produkt["Ilosc"] >= ilosc:
                        produkt["Ilosc"] -= ilosc
                        salo_sklepu += float(produkt["Cena"]) * ilosc
                        historia_operacji.append(f"sprzedaż: {produkt['Nazwa_produktu']}, {ilosc} szt., {float(produkt['Cena']) * ilosc} PLN")
                        print(f"Sprzedano {ilosc} sztuk. Saldo zaktualizowane.")
                    else:
                        print("Brak wystarczającej ilości towaru na magazynie.")
            if not znaleziono_produkt:
                print("Nie znaleziono produktu o podanym ASIN.")
        case "3":
            nazwa_produktu = input("Podaj nazwę produktu do zakupu: ")
            cena = float(input("Podaj cenę produktu: "))
            ilosc = int(input("Podaj liczbę sztuk do zakupu: "))
            if salo_sklepu >= cena * ilosc:
                znaleziono_produkt = False
                for produkt in zbor_produktow:
                    if produkt["Nazwa_produktu"].lower() == nazwa_produktu.lower():
                        produkt["Ilosc"] += ilosc
                        znaleziono_produkt = True
                        break
                if not znaleziono_produkt:
                    asin = input("Podaj numer ASIN dla nowego produktu: ")
                    rok_produkcji = input("Podaj rok produkcji dla nowego produktu: ")
                    zbor_produktow.append({
                        "Nazwa_produktu": nazwa_produktu,
                        "Rok_Produkcji": rok_produkcji,
                        "Cena": str(cena),
                        "Ilosc": ilosc,
                        "ASIN": asin
                    })
                salo_sklepu -= cena * ilosc
                historia_operacji.append(f"zakup: {nazwa_produktu}, {ilosc} szt., {cena * ilosc} PLN")
                print("Zakupiono. Saldo zaktualizowane.")
            else:
                print("Za mało środków na koncie.")
        case "4":
            print(f"Aktualne konto: {salo_sklepu} PLN")
        case "5":
            print("Stan magazynu:")
            for produkt in zbor_produktow:
                print(f"{produkt['Nazwa_produktu']} - {produkt['Ilosc']} szt., cena: {produkt['Cena']} PLN")
        case "6":
            nazwa_produktu = input("Podaj nazwę produktu: ")
            znaleziono_produkt = False
            for produkt in zbor_produktow:
                if produkt["Nazwa_produktu"].lower() == nazwa_produktu.lower():
                    print(f"Stan magazynu dla produktu {nazwa_produktu}: {produkt['Ilosc']} szt., cena: {produkt['Cena']} PLN")
                    znaleziono_produkt = True
                    break
            if not znaleziono_produkt:
                print("Nie znaleziono produktu o podanej nazwie.")
        case "7":
            od = input("Podaj indeks początkowy (pusty dla początku): ")
            do = input("Podaj indeks końcowy (pusty dla końca): ")
            if od == "":
                od_index = 0
            else:
                od_index = int(od)
            if do == "":
                do_index = len(historia_operacji)
            else:
                do_index = int(do) + 1
            print(f"Przegląd operacji od {od_index} do {do_index - 1}:")
            for operacja in historia_operacji[od_index:do_index]:
                print(operacja)
        case "8":
            print("Koniec działania programu.")
            break
