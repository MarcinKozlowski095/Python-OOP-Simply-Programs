"""
Zadanie 7: Klasa Course i Student
Stwórz klasę Course, która przechowuje nazwę kursu i listę zapisanych studentów.
Następnie stwórz klasę Student, która przechowuje imię, nazwisko i numer identyfikacyjny.
Dodaj metody do zapisywania studenta na kurs oraz do wyświetlania listy studentów zapisanych na dany kurs.
"""

class Course:
    def __init__(self, course_name):
        self.coure_name = course_name
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def display(self):
        for student in self.student_list:
            print(student)

class Student:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

course = Course('IT')
student1 = Student('Joe', 'Doe', 123)
student2 = Student('John', 'Smith', 789)
course.add_student(student1)
course.add_student(student2)
course.display()
