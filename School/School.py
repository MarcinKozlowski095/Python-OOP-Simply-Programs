"""
Zadanie 9: Klasa School i Teacher
Stwórz klasę School, która przechowuje nazwę szkoły i listę nauczycieli.
Następnie stwórz klasę Teacher, która przechowuje imię, nazwisko i przedmiot nauczany.
Dodaj metody do dodawania i usuwania nauczycieli oraz wyświetlania listy nauczycieli w szkole.
"""

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
            return f'Teacher {teacher.first_name} {teacher.last_name} has been added.'
        else:
            return f'Teacher {teacher.first_name} {teacher.last_name} is already in the list.'

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            return f'Teacher {teacher.first_name} {teacher.last_name} has been removed.'
        else:
            return f'Teacher {teacher.first_name} {teacher.last_name} is not in the list.'

    def display(self):
        return self.teachers

class Teacher:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.subject}'



school = School("Green Valley High School")
teacher1 = Teacher("John", "Smith", "Mathematics")
teacher2 = Teacher("Jane", "Doe", "Physics")
teacher3 = Teacher("Emily", "Clark", "Chemistry")

print(school.add_teacher(teacher1))
print(school.add_teacher(teacher2))
print(school.add_teacher(teacher3))
print(school.add_teacher(teacher1))  

print(school.display())

print(school.remove_teacher(teacher1))
print(school.remove_teacher(teacher1))

print(school.display())
