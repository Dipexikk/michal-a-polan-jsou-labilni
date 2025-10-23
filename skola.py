class person:
    _id_pocitadlo = 1

    def __init__(self, id: int, name: str, surname: str, age: int, gender: str):
        self.id = person._id_pocitadlo
        person._id_pocitadlo += 1


        self.name = str(name)
        self.surname = str(surname)
        self.age = int(age)
        self.gender = str(gender)

    def Vypis(self):
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.name}\n"
            f"Příjmení: {self.surname}\n"
            f"Věk: {self.age}\n"
            f"Pohlaví: {self.gender}\n"
        )
    
class student(person):
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str, student_class: str, obor: str):
        super().__init__(id, name, surname, age, gender)
        self.student_class = str(student_class)
        self.obor = str(obor)

    def Vypis(self):
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.name}\n"
            f"Příjmení: {self.surname}\n"
            f"Věk: {self.age}\n"
            f"Pohlaví: {self.gender}\n"
            f"Třída: {self.student_class}\n"
            f"Obor: {self.obor}\n"
        )

class employee(person):
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str, salary: float, position: str):
        super().__init__(id, name, surname, age, gender)
        self.salary = float(salary)
        self.position = str(position)

    def Vypis(self):
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.name}\n"
            f"Příjmení: {self.surname}\n"
            f"Věk: {self.age}\n"
            f"Pohlaví: {self.gender}\n"
            f"Plat: {self.salary}Kč\n"
            f"Pozice: {self.position}\n"
        )


    

person_list = [
    employee(1, "Petr", "Breit", 26, "Male", 20000, "Učitel"),
    employee(2, "Lenka", "Zedníková", 41, "Female", 36000, "Učitelka"),
    employee(3, "Petr", "Leba", 46, "Male", 42000, "Sigma"),
    student(1, "Daniel", "Polan", 18, "Male", "IT3A", "IT"),
    student(1, "Martin", "Šedivec", 19, "Male", "IT3A", "IT"),
    student(6, "Jakub", "Kořínský", 18, "Male", "IT4B", "IT"),
]

for zam in person_list:
        print(zam.vypis)
        print("-" * 50)

        if isinstance(person, student):
            person.studovat()
        elif isinstance(person, employee):
            person.vyucovat()
