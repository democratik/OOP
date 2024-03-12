class Operacja:
    def wykonaj(self, a, b):
        pass

class Dodawanie(Operacja):
    def wykonaj(self, a, b):
        return a + b

class Odejmowanie(Operacja):
    def wykonaj(self, a, b):
        return a - b

class Mnozenie(Operacja):
    def wykonaj(self, a, b):
        return a * b

class Dzielenie(Operacja):
    def wykonaj(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Błąd! Dzielenie przez zero."

def kalkulator():
    a = float(input("Wprowadź pierwszą liczbę: "))
    operacja = input("Wprowadź operację (+, -, *, /): ")
    b = float(input("Wprowadź drugą liczbę: "))

    if operacja == '+':
        wynik = Dodawanie().wykonaj(a, b)
    elif operacja == '-':
        wynik = Odejmowanie().wykonaj(a, b)
    elif operacja == '*':
        wynik = Mnozenie().wykonaj(a, b)
    elif operacja == '/':
        wynik = Dzielenie().wykonaj(a, b)
    else:
        wynik = "Nieznana operacja!"

    print(f"Wynik: {wynik}")

kalkulator()



