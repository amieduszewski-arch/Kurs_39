class Uczen:
    def __init__(self, imie, nazwisko, klas):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klas = klas

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot_prowadzony, lista_klasow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot_prowadzony = przedmiot_prowadzony
        self.lista_klasow = lista_klasow

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"


class Wychowawca:
    def __init__(self, imie, nazwisko, klas):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klas = klas

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"


szkola = {
    "uczeniowie": [
        Uczen("Jan", "Kowalski", "3C"),
        Uczen("Anna", "Nowak", "3C"),
        Uczen("Piotr", "Zielinski", "2B")
    ],

    "nauczyciel": [
        Nauczyciel("Maria", "Kowal", "Matematyka", ["3C", "2B"]),
        Nauczyciel("Tomasz", "Lis", "Historia", ["3C"])
    ],

    "wychowawca": [
        Wychowawca("Daria", "Malik", "3C"),
        Wychowawca("Adam", "Nowicki", "2B")
    ]
}


def wyszukaj_uczniow_klasy(lista_uczniow, klas):
    wynik = []
    for uczen in lista_uczniow:
        if uczen.klas == klas:
            wynik.append(uczen)
    return wynik


def wyszukaj_wychowawce_klasy(lista_wychowawcow, klas):
    for wych in lista_wychowawcow:
        if wych.klas == klas:
            return wych
    return None


def wyszukaj_lekcje_ucznia(imie, nazwisko):
    klas_ucznia = None
    for uczen in szkola["uczeniowie"]:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            klas_ucznia = uczen.klas

    if klas_ucznia is None:
        return

    for nauczyciel in szkola["nauczyciel"]:
        if klas_ucznia in nauczyciel.lista_klasow:
            print(nauczyciel.przedmiot_prowadzony, nauczyciel.imie, nauczyciel.nazwisko)


while True:
    wybierz_potrzebna_opcje = input("Wybierz opcje:\n1. Utwórz\n2. Zarządzaj\n3. Koniec\n")

    if wybierz_potrzebna_opcje == "1":
        while True:
            obiekt_do_dodania = input("Kogo chcesz dodac:\n1. Uczen\n2. Nauczyciel\n3. Wychowawca\n4. Koniec\n")

            match obiekt_do_dodania:
                case "1":
                    imie_ucznia = input("Podaj imie ucznia: ")
                    nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
                    klas_ucznia = input("Podaj klase ucznia: ")
                    uczen = Uczen(imie_ucznia, nazwisko_ucznia, klas_ucznia)
                    szkola["uczeniowie"].append(uczen)

                case "2":
                    imie_nauczyciela = input("Podaj imie nauczyciela: ")
                    nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
                    przedmiot = input("Podaj przedmiot: ")
                    lista_klasow = []
                    while True:
                        klasa = input("Podaj klase (Enter konczy): ")
                        if not klasa:
                            break
                        lista_klasow.append(klasa)
                    nauczyciel = Nauczyciel(imie_nauczyciela, nazwisko_nauczyciela, przedmiot, lista_klasow)
                    szkola["nauczyciel"].append(nauczyciel)

                case "3":
                    imie = input("Podaj imie wychowawcy: ")
                    nazwisko = input("Podaj nazwisko wychowawcy: ")
                    klas = input("Prowadzona klasa: ")
                    wychowawca = Wychowawca(imie, nazwisko, klas)
                    szkola["wychowawca"].append(wychowawca)

                case "4":
                    break

    elif wybierz_potrzebna_opcje == "2":
        while True:
            opcja_do_edycji = input("Czym chcesz zarządzac:\n1. Klasa\n2. Uczen\n3. Nauczyciel\n4. Wychowawca\n5. Koniec\n")

            match opcja_do_edycji:
                case "1":
                    numer_klasy = input("Podaj klase: ")
                    uczniowie = wyszukaj_uczniow_klasy(szkola["uczeniowie"], numer_klasy)
                    wychowawca = wyszukaj_wychowawce_klasy(szkola["wychowawca"], numer_klasy)
                    print(f"Uczniowie klasy {uczniowie}")
                    print(f"Wychowawca klasy {wychowawca}")

                case "2":
                    imie = input("Podaj imie ucznia: ")
                    nazwisko = input("Podaj nazwisko ucznia: ")
                    wyszukaj_lekcje_ucznia(imie, nazwisko)

                case "3":
                    imie = input("Podaj imie nauczyciela: ")
                    nazwisko = input("Podaj nazwisko nauczyciela: ")
                    for nauczyciel in szkola["nauczyciel"]:
                        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
                            print(f"Prowadzi klasy {nauczyciel.lista_klasow}")

                case "4":
                    imie = input("Podaj imie wychowawcy: ")
                    nazwisko = input("Podaj nazwisko wychowawcy: ")

                    for wych in szkola["wychowawca"]:
                        if wych.imie == imie and wych.nazwisko == nazwisko:
                            uczniowie = wyszukaj_uczniow_klasy(szkola["uczeniowie"], wych.klas)
                            print(f"Uczniowie, których prowadzi wychowawca {uczniowie}")

                case "5":
                    break

    elif wybierz_potrzebna_opcje == "3":
        break