from funkcje import nastepny_dzien
from file_handler import WeatherForecast

miasto = input("Podaj nazwę miasta: ")
data = input("Podaj datę (RRRR-MM-DD) lub zostaw puste: ")

if data.strip() == "":
    data = nastepny_dzien()

weather_forecast = WeatherForecast(miasto)

wynik = weather_forecast[data]
print("Prognoza:", wynik)

print("Daty zapisane w pliku:")
for d in weather_forecast:
    print(d)

print("Zapisane wyniki (data, pogoda):")
for x in weather_forecast.items():
    print(x)