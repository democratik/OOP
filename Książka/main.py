class Ksiazka:
    def __init__(self, tytuł, autor , rok_wydania):
        self.tytuł = tytuł
        self.autor  = autor
        self.rok_wydania = rok_wydania

    def display_info(self):
        print(f"tytuł: {self.tytuł}, autor: {self.autor }, rok_wydania: {self.rok_wydania}")

K1 = Ksiazka("Samochód", "Ja", 2023)
K2 = Ksiazka("Pogoda", "Nie ja", 2024)
K3 = Ksiazka("Laptopy", "Pan", 2019)

K1.display_info()
K2.display_info()
K3.display_info()