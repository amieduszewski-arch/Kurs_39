import datetime

print("hello wordl")

Imie = input("Podaj imię: ")
Rok_urodzenia = int(input("Podaj rok urodzenia: "))
Wiadomosc = input("Napisz swoje zyczenia: ")
Imie_nadacy = input("Podaj imie nadacy: ")

obecny_rok = datetime.datetime.now().year
wiek = obecny_rok - Rok_urodzenia


print(f"{Imie}, wszystkiego najlepszego z okazji {wiek} urodzin!")
print(f"{Wiadomosc}")
print(f"{Imie_nadacy}")
