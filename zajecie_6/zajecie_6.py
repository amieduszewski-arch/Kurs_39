# def przywitaj_sie():
#     print("Witaj w swiecie")
#
# def sprawdz_wiek(wiek):
#     if wiek < 18:
#         print("Jestes niepelnoletni/a")
#     else:
#         print("mozesz kupic alkohol!")
#
# def sprawdz_wiek_i_przywiaj_sie(wiek, imie):
#     if wiek < 18:
#         print("Jestes niepelnoletni/a")
#     else:
#         print("Mozesz kupic alkohol")
#     print(f"Witaj {imie}")
#
# wiek_urzedkownika = int(input("Podaj swoj wiek: "))
#
# sprawdz_wiek(wiek_urzedkownika)
#
# nazwa_uzytkowika = input("Podaj swoje imie: ")
#
# sprawdz_wiek_i_przywiaj_sie(wiek_urzedkownika, nazwa_uzytkowika)


def obliczenie_temperatury_w_fehrenheitach(temperatura_w_celsjuszach):
    temperatura_w_fahrenheit = temperatura_w_celsjuszach * 9 / 5 + 32
    print(f"Tempteratura w fahreinach: {temperatura_w_fahrenheit}")


obliczenie_temperatury_w_fehrenheitach(1)
