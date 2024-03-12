class Samochod:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def display_info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}")

bmw = Samochod("BMW", "X5", 2020)
volvo = Samochod("Volvo", "XC60", 2018)
jeep = Samochod("Jeep", "Wrangler", 2021)

bmw.display_info()
volvo.display_info()
jeep.display_info()