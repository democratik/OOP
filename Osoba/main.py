class Osoba:

    def person(self, name="Piotr", sekond_name="Laptop", age=25):
        self.name = name
        self.age = age
        self.sekond_name = sekond_name

    def display_info(self):
        print(f"Imię: {self.name}, Drugie imię: {self.sekond_name}, Wiek: {self.age}")

osoba = Osoba()
osoba.person("Jan", "Kowalski", 30)
osoba.display_info()