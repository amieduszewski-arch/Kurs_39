from file_handler import file_handler

saldo_sklepu = file_handler.saldo
historia_operacji = file_handler.historia
zbor_produktow = file_handler.produkty


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
            srodki = float(
                input("Podaj kwotę do doładowania (lub ujemną do odjęcia): ")
            )
            if saldo_sklepu + srodki < 0:
                print("Nie możesz ustawić salda na wartość ujemną.")
            else:
                saldo_sklepu += srodki
                historia_operacji.append(f"saldo: {srodki}")
                print(f"Aktualne saldo wynosi: {saldo_sklepu} PLN")
        case "2":
            numer_asin = input("Podaj numer ASIN produktu do sprzedaży: ")
            znaleziono_produkt = False
            for produkt in zbor_produktow:
                if produkt.get("ASIN") == numer_asin:
                    znaleziono_produkt = True
                    ilosc = int(input("Podaj liczbę sztuk do sprzedaży: "))
                    if produkt["Ilosc"] >= ilosc:
                        produkt["Ilosc"] -= ilosc
                        saldo_sklepu += float(produkt["Cena"]) * ilosc
                        historia_operacji.append(
                            f"sprzedaż: {produkt['Nazwa_produktu']}, {ilosc} szt., {float(produkt['Cena']) * ilosc} PLN"
                        )
                        print(f"Sprzedano {ilosc} sztuk. Saldo zaktualizowane.")
                    else:
                        print("Brak wystarczającej ilości towaru na magazynie.")
            if not znaleziono_produkt:
                print("Nie znaleziono produktu o podanym ASIN.")
        case "3":
            nazwa_produktu = input("Podaj nazwę produktu do zakupu: ")
            cena = float(input("Podaj cenę produktu: "))
            ilosc = int(input("Podaj liczbę sztuk do zakupu: "))
            if saldo_sklepu >= cena * ilosc:
                znaleziono_produkt = False
                for produkt in zbor_produktow:
                    if produkt["Nazwa_produktu"].lower() == nazwa_produktu.lower():
                        produkt["Ilosc"] += ilosc
                        znaleziono_produkt = True
                        break
                if not znaleziono_produkt:
                    asin = input("Podaj numer ASIN dla nowego produktu: ")
                    rok_produkcji = input("Podaj rok produkcji dla nowego produktu: ")
                    zbor_produktow.append(
                        {
                            "Nazwa_produktu": nazwa_produktu,
                            "Rok_Produkcji": rok_produkcji,
                            "Cena": str(cena),
                            "Ilosc": ilosc,
                            "ASIN": asin,
                        }
                    )
                saldo_sklepu -= cena * ilosc
                historia_operacji.append(
                    f"zakup: {nazwa_produktu}, {ilosc} szt., {cena * ilosc} PLN"
                )
                print("Zakupiono. Saldo zaktualizowane.")
            else:
                print("Za mało środków na koncie.")
        case "4":
            print(f"Aktualne konto: {saldo_sklepu} PLN")
        case "5":
            print("Stan magazynu:")
            for produkt in zbor_produktow:
                print(
                    f"{produkt['Nazwa_produktu']} - {produkt['Ilosc']} szt., cena: {produkt['Cena']} PLN"
                )
        case "6":
            nazwa_produktu = input("Podaj nazwę produktu: ")
            znaleziono_produkt = False
            for produkt in zbor_produktow:
                if produkt["Nazwa_produktu"].lower() == nazwa_produktu.lower():
                    print(
                        f"Stan magazynu dla produktu {nazwa_produktu}: {produkt['Ilosc']} szt., cena: {produkt['Cena']} PLN"
                    )
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

file_handler.save_data_to_file(new_saldo=saldo_sklepu, new_historia=historia_operacji, new_produkty=zbor_produktow)