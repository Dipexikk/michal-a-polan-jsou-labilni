import random

class Zamestnanec:
    def __init__(self, jmeno: str, prijmeni: str, pozice: str, plat: float, vek: int, oddeleni: str):
        self.id = self.generuj_id()
        self.jmeno = str(jmeno)
        self.prijmeni = str(prijmeni)
        self.pozice = str(pozice)
        self.plat = float(plat)
        self.vek = int(vek)
        self.oddeleni = str(oddeleni)


    def generuj_id(self):
        return random.randint(1000, 9999)

    def info(self):
        return f"{self.jmeno} {self.prijmeni}, {self.pozice}, Plat: {self.plat} Kč, Věk: {self.vek} let"

    def rocni_plat(self):
        return self.plat * 12

    def narozeniny(self):
        if self.vek > 50:
            return f"Vše nejlepší k narozeninám, {self.jmeno}!"
        return "Žádné speciální přání."

zamestnanci = [
    Zamestnanec("Petr", "Novák", "Programátor", 45000, 30, "IT"),
    Zamestnanec("Jana", "Svobodová", "HR Specialist", 35000, 28, "Lidské zdroje"),
    Zamestnanec("Martin", "Novotný", "Manager", 60000, 45, "Obchod"),
    Zamestnanec("Alice", "Horáková", "Analytik", 47000, 32, "Finance"),
    Zamestnanec("Jan", "Kříž", "Designér", 40000, 27, "Marketing"),
    Zamestnanec("Eva", "Vlachová", "Testovací inženýr", 39000, 50, "IT"),
    Zamestnanec("Tomáš", "Pavelka", "CEO", 150000, 55, "Management"),
    Zamestnanec("Lucie", "Dvořáková", "Asistentka", 25000, 24, "Administrativa"),
    Zamestnanec("Marek", "Bartoš", "Konzultant", 55000, 38, "Obchod"),
    Zamestnanec("Karel", "Müller", "Finanční analytik", 52000, 43, "Finance")
]

for zamestnanci in zamestnanci:
    print(f"ID: {zamestnanci.id} - {zamestnanci.info()}")
    print(f"Roční plat: {zamestnanci.rocni_plat()} Kč")
    print(zamestnanci.narozeniny())
    print("-" * 40)
