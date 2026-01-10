from funkcje import sprawdz_opady, nastepny_dzien

miasto = input("Podaj nazwę miasta: ")
data = input("Podaj datę (RRRR-MM-DD) lub pozostaw puste: ")

if data.strip() == "":
    data = nastepny_dzien()

wynik = sprawdz_opady(miasto, data)

print(wynik)