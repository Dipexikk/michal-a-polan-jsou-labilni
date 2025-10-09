class Zamestnanec:
    _id_pocitadlo = 1  
 
    def __init__(self, jmeno: str, prijmeni: str, vek: int, pozice: str, plat: float, oddeleni: str):
        self.id = Zamestnanec._id_pocitadlo
        Zamestnanec._id_pocitadlo += 1
 
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.pozice = pozice
        self.plat = plat
        self.oddeleni = oddeleni
 
    def plny_nazev(self):
        return f"{self.jmeno} {self.prijmeni}"
 
    def rocni_prijem(self):
        return self.plat * 12
 
    def vypis(self):
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.jmeno}\n"
            f"Příjmení: {self.prijmeni}\n"
            f"Věk: {self.vek}\n"
            f"Pozice: {self.pozice}\n"
            f"Plat: {self.plat} Kč\n"
            f"Oddělení: {self.oddeleni}\n"
            f"Roční příjem: {self.rocni_prijem()} Kč"
        )
 
 
seznam_zamestnancu = [
    Zamestnanec("Jan", "Novak", 30, "Programátor", 50000, "IT"),
    Zamestnanec("Eva", "Svobodova", 28, "Grafička", 45000, "Marketing"),
    Zamestnanec("Petr", "Kral", 40, "Manažer", 70000, "Prodej"),
    Zamestnanec("Anna", "Horakova", 35, "Účetní", 48000, "Finance"),
    Zamestnanec("Karel", "Marek", 50, "Technická podpora", 42000, "IT"),
    Zamestnanec("Lucie", "Dvorakova", 29, "Personalistka", 47000, "HR"),
    Zamestnanec("Michal", "Bilek", 32, "Vývojář", 52000, "IT"),
    Zamestnanec("Petra", "Sedlakova", 31, "Marketingová specialistka", 46000, "Marketing"),
    Zamestnanec("Jiri", "Svoboda", 45, "Projektový manažer", 68000, "Projekty"),
    Zamestnanec("Martina", "Novotna", 27, "Asistentka", 38000, "Administrativa"),
]
 
for zam in seznam_zamestnancu:
    print(zam.vypis())
    print("----------------------")
 