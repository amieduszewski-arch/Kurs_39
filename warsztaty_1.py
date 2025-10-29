print("Hello World")
#
# wiek_michala = int(input("Michal prosze podaj swoj wiek?: "))
# wiek_ani = int(input("Ania prosze podaj swoj wiek: "))
#
# print(f"Czy Michal jest starszy od Ani? {wiek_michala > wiek_ani}")
# print(f"Czy Ania jest mlodsza czy rowna wieku Michala? {wiek_michala <= wiek_ani}")
# print(f"Czy maja tyle samo lat? {wiek_michala == wiek_ani}")
#from zajecia_1.hello_world import cena_jabka

#zadanie 2

# print("Hello World")
#
# jabko = float(input("Podaj cene jablka: "))
# pomarancza = float(input("Podaj cene pomarancza: "))
# banan = float(input("Podaj cene banana: "))
#
# print(f"Czy jablko jest tansze od Pomarancze? {jabko < pomarancza}")
# print(f"Czy pomarancza jes drozdza od banana? {pomarancza > banan}")
# print(f"Czy jabko i banan kosztuje tyle samo? {jabko == banan}")
# print(f"Czy jabko jest tansze od pomaranczy lub rowne bananowi? {jabko < pomarancza} or {jabko == banan}")
# print(f"Czy pomarancza jest drozsza od jablka i banana jednoczesnie? {pomarancza > (jabko + banan)}")

# Zadanie 3 — Logiczne fakty o pogodzie

# print("1 = tak")
# print("0 = nie")
#
# jest_ceplo = bool(int(input("Czy jest cieplo?: ")))
# pada_deszcz = bool(int(input("Czy pada deszcz?: ")))
# wieje_wiatr = bool(int(input("Czy wieje wiatr?: ")))
#
# print(f"Czy jest dobra pogowa na spacer? {jest_ceplo and not pada_deszcz}")
# print(f"Czy lepiej zostac w domu? {not jest_ceplo or pada_deszcz}")
# print(f"Czy pada albo wieje? {pada_deszcz or wieje_wiatr}")
# print(f"czy nie pada? {not pada_deszcz}")
# print(f"Czy jest cieplo, ale nie pada i nie wieje {jest_ceplo and not pada_deszcz and not wieje_wiatr}")

#zadanie 4

# wiek =int(input("Podaj swoj wiek: "))
# waga = float(input("Podaj swoja wage: "))
#
# wiek += 5
# waga += 2.3
#
# print(f"Waga: {waga} typ: {type(waga)}")
# print(f"Wiek: {wiek} typ: {type(wiek)}")

#zadanie 5 ???

# cukierki = int(input("Podaj liczbe cukierkow: "))
# dzieci = int(input("Podaj liczbe dzieci: "))
#
# na_dziecko = cukierki // dzieci
# reszta = cukierki & dzieci
#
# print(f"Jedno dziecko dostanie: {na_dziecko}")
# print(f"Zostanie: {reszta}")
# print(f"czy cukierkow wystarczy dla wszystkich dzieci: {cukierki >= dzieci}")
# print(f"Czy cukierkow jest mniej niz 10 lub wiecej niz 100 {cukierki < 10 or cukierki > 100}")

#zadanie 6

jajko = int(input("Ile sztuk jajek?: "))
cena_jajka = float(input("Podaj cene jajek?: "))

jablko = int(input("Ile sztuk jablek?: "))
cena_jabka = float(input("Podaj cene jablka?: "))

grusza = int(input("Ile sztuk grusz?: "))
cena_gruszy = float(input("Podaj cene gruszy?: "))

budzet = float(input("Podaj swoj budzet?: "))

suma = jajko * cena_jajka + jablko * cena_jabka + grusza * cena_gruszy

print(f"Suma zakupow? {suma}")

print(f"Budzet {budzet}")

print(f"Suma wieksza od budzetu? {budzet < suma}")

print(f"Liczba sztuk wiecej niz 10? {jajko + jablko + grusza > 10}")

print(f"Czy zadna cena nie jest 0? {cena_gruszy == 0 or cena_jajka == 0 or cena_jabka}")

print(f"Ceny > 0? {cena_jabka > 0 or cena_jajka > 0 or cena_gruszy > 0}")

print(f"Czy jakis produkt jest drozszy od innego 2x {
cena_gruszy > 2 * cena_jajka or cena_gruszy > 2 * cena_jabka or cena_jajka > 2 * cena_jabka
}")