from funkcje import sprawdz_opady

miasto = input("Podaj nazwę miasta: ")
data = input("Podaj datę (RRRR-MM-DD) lub zostaw puste: ")

wynik = sprawdz_opady(miasto, data)

print("Wynik:", wynik)