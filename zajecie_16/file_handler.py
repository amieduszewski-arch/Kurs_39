from funkcje import wczytaj_wyniki, zapisz_wyniki, sprawdz_opady


class WeatherForecast:

    def __init__(self, miasto):
        self.miasto = miasto
        self.dane = wczytaj_wyniki()
        if miasto not in self.dane:
            self.dane[miasto] = {}

    def __getitem__(self, data):
        if data in self.dane[self.miasto]:
            return self.dane[self.miasto][data]
        wynik = sprawdz_opady(self.miasto, data)
        self.dane = wczytaj_wyniki()
        return wynik

    def __setitem__(self, data, pogoda):
        self.dane = wczytaj_wyniki()
        if self.miasto not in self.dane:
            self.dane[self.miasto] = {}
        self.dane[self.miasto][data] = pogoda
        zapisz_wyniki(self.dane)

    def __iter__(self):
        return iter(self.dane[self.miasto].keys())

    def items(self):
        for data in self.dane[self.miasto]:
            yield (data, self.dane[self.miasto][data])