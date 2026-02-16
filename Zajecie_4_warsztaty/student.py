# Napisz program, który policzy statystyki dotyczące ocen studentów.
#
# Program działa tak:
#   1) Pyta użytkownika: "Ile ocen chcesz podać?" gotowe
#   2) Wczytuje kolejno oceny (każda w osobnej linii) gotowe
#
# ZASADY:
# - Ocena może być od 2 do 5 (włącznie).
# - Jeśli użytkownik poda ocenę spoza zakresu (np. 1 albo 6),
#     → program natychmiast kończy wczytywanie
#     → i liczy statystyki tylko z poprawnych ocen.
#
# PROGRAM MA WYPISAĆ:
#   1) Ile poprawnych ocen wczytano.
#   2) Ile było ocen niedostatecznych (2).
#   3) Ile było "dobrych" ocen: 4 lub 5.
#   4) Średnią arytmetyczną poprawnych ocen.
#
# Przykład:
#     Wejście:
#         5
#         3
#         4
#         5
#         1
#
#     Wynik:
#         Wczytano 3 poprawnych ocen
#         Niedostatecznych: 0
#         Dobrych (4 lub 5): 2
#         Średnia: 4.0
#
# ==========================================

ilosc_ocen = int(input("Ile ocen chcesz podać?: "))

poprawne_oceny = 0
niedostatecznych = 0
dobra_ocena = 0
suma_ocen = 0

for i in range(ilosc_ocen):
    ocena = int(input(f"Podaj ocenę {i + 1}: "))
    if ocena < 2 or ocena > 5:
        print("Ocena może być tylko od 2 do 5.")
        break
    poprawne_oceny += 1
    suma_ocen += ocena

    if ocena == 2:
        niedostatecznych += 1
    if ocena == 4 or ocena == 5:
        dobra_ocena += 1


print("---PODSUMOWANIE---")
print(f"Wczytano {poprawne_oceny} poprawnych ocen.")
print(f"Niedostatecznych {niedostatecznych}")
print(f"Dobrych (4 lub 5): {dobra_ocena}")
print(f"Średnia: {suma_ocen / poprawne_oceny}")
