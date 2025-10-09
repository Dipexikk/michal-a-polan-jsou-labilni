class person:
    _id_pocitadlo = 1

    def __init__(self, id, name, surname, age, gender):
        self.id = person._id_pocitadlo
        person._id_pocitadlo += 1


        self.name = (name)
        self.surname = (surname)
        self.age = (age)
        self.gender = (gender)

class student(person):
    def __init__(self, id, name, surname, age, gender, student_class):
        super().__init__(self, id, name, surname, age, gender)
        self.student_class = (student_class)


class employee(person):
    def __init__(self, id, name, surname, age, gender, salary):
        super().__init__(self, id, name, surname, age, gender)
        self.salary = (salary)



def Vypis(self):
    return (
        f"ID: {self.id}\n"
        f"Jméno: {self.name}\n"
        f"Příjmení: {self.surname}\n"
        f"Věk: {self.age}\n"
        f"Pohlaví: {self.gender}\n"
    )

person_list = [
    employee("Petr", "Breit", 26, "Male", 42000),
    employee("Lenka", "Zedníková", 41, "Female", 36000),
    employee("Petr", "Leba", 46, "Male", 42000),
    student("Daniel", "Polan", 18, "Male", "IT3A"),
    student("Martin", "Šedivec", 19, "Male", "IT3A"),
    student("Jakub", "Kořínský", 18, "Male", "IT4B"),
]


for zam in person_list:
    print(zam.vypis())
    print("----------------------")