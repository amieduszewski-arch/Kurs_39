import json
import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta


def wczytaj_dane():
    try:
        with open("dane.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def zapisz_dane(dane):
    with open("dane.json", "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=4)


def pobierz_wspolrzedne(miasto):
    geolocator = Nominatim(user_agent="szkolny_program")
    location = geolocator.geocode(miasto)
    if location is None:
        return None, None
    return location.latitude, location.longitude


def sprawdz_api(latitude, longitude, searched_date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

    response = requests.get(url)
    if response.status_code != 200:
        return "nie wiem"

    data = response.json()

    try:
        rain_value = data["daily"]["rain_sum"][0]
    except Exception:
        return "nie wiem"

    if rain_value is None:
        return "nie wiem"
    if rain_value < 0:
        return "nie wiem"
    if rain_value == 0:
        return "nie pada"
    if rain_value > 0:
        return "pada"

    return "nie wiem"


def sprawdz_opady(miasto, searched_date=None):
    if searched_date == "" or searched_date is None:
        searched_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    dane = wczytaj_dane()

    if miasto in dane and searched_date in dane[miasto]:
        return dane[miasto][searched_date]

    latitude, longitude = pobierz_wspolrzedne(miasto)

    if latitude is None:
        return "nie wiem"

    wynik = sprawdz_api(latitude, longitude, searched_date)

    if miasto not in dane:
        dane[miasto] = {}

    dane[miasto][searched_date] = wynik
    zapisz_dane(dane)

    return wynik