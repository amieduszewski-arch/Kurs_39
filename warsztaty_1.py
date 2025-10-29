# print("Hello World")
#
# wiek_michala = int(input("Michal prosze podaj swoj wiek?: "))
# wiek_ani = int(input("Ania prosze podaj swoj wiek: "))
#
# print(f"Czy Michal jest starszy od Ani? {wiek_michala > wiek_ani}")
# print(f"Czy Ania jest mlodsza czy rowna wieku Michala? {wiek_michala <= wiek_ani}")
# print(f"Czy maja tyle samo lat? {wiek_michala == wiek_ani}")

print("Hello World")

jabko = float(input("Podaj cene jablka: "))
pomarancza = float(input("Podaj cene pomarancza: "))
banan = float(input("Podaj cene banana: "))

print(f"Czy jablko jest tansze od Pomarancze? {jabko < pomarancza}")
print(f"Czy pomarancza jes drozdza od banana? {pomarancza > banan}")
print(f"Czy jabko i banan kosztuje tyle samo? {jabko == banan}")
print(f"Czy jabko jest tansze od pomaranczy lub rowne bananowi? {jabko < pomarancza} or {jabko == banan}")
print(f"Czy pomarancza jest drozsza od jablka i banana jednoczesnie? {pomarancza > (jabko + banan)}")