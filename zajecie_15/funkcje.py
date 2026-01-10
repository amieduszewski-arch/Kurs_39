import json
import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta


plik = "dane_pogodowe.json"


def wczytaj_wyniki():
    with open(plik, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def zapisz_wyniki(dane):
    with open(plik, "w", encoding="utf-8") as f:
        f.write(json.dumps(dane, ensure_ascii=False, indent=4))


def pobierz_wspolrzedne(miasto):
    geolocator = Nominatim(user_agent="aleksander_app")
    location = geolocator.geocode(miasto)

    if location is None:
        return None, None

    return location.latitude, location.longitude


def sprawdz_opady(miasto, data):
    wyniki = wczytaj_wyniki()

    if miasto in wyniki:
        for zapisana_data in wyniki[miasto]:
            if zapisana_data == data:
                return wyniki[miasto][data]

    latitude, longitude = pobierz_wspolrzedne(miasto)

    if latitude is None or longitude is None:
        wynik = "Nie wiem"
    else:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={data}&end_date={data}"

        response = requests.get(url)
        dane = response.json()

        if "daily" in dane and "rain_sum" in dane["daily"]:
            rain_value = dane["daily"]["rain_sum"][0]

            if rain_value > 0.0:
                wynik = "Będzie padać"
            elif rain_value == 0.0:
                wynik = "Nie będzie padać"
            else:
                wynik = "Nie wiem"
        else:
            wynik = "Nie wiem"

    if miasto not in wyniki:
        wyniki[miasto] = {}

    wyniki[miasto][data] = wynik
    zapisz_wyniki(wyniki)

    return wynik


def nastepny_dzien():
    jutro = datetime.now().date() + timedelta(days=1)
    return str(jutro)