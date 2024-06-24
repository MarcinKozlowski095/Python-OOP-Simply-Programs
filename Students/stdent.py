"""
Zadanie: System Zarządzania Studentami
Napisz klasy dla systemu zarządzania studentami.
Klasa Student powinna mieć atrybuty jak imie, nazwisko, nr_indeksu, oraz przedmioty.
Klasa Przedmiot powinna zawierać nazwa, prowadzacy, oraz oceny.
Dodaj klasę Dziennik, która będzie zarządzać studentami i przedmiotami oraz umożliwiać dodawanie ocen.
"""

class Student:
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number
        self.subjects = {}

    def add_subject(self, subject):
        if subject.name not in self.subjects:
            self.subjects[subject.name] = subject

    def remove_subject(self, subject):
        if subject.name in self.subjects:
            del self.subjects[subject.name]

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.subjects[subject.name].append(grade)

    def display_grades(self):
        print(f'Student: {self.first_name} {self.last_name}, Index number: {self.index_number}')
        for subject_name, subject in self.subjects.items():
            subject.display_grades()  

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display_grades(self):
        print(f'Course grades {self.name}: {self.grades}')

class Diary:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def display_students(self):
        for student in self.students:
            print(f'Student: {student.first_name} {student.last_name}, Index number: {student.index_number}')



student1 = Student("Adam", "Nowak", "12345")
student2 = Student("Anna", "Kowalska", "54321")


subject1 = Subject("Matematyka", "Jan Kowalski")
subject2 = Subject("Informatyka", "Maria Nowak")


student1.add_subject(subject1)
student1.add_subject(subject2)
student2.add_subject(subject1)


subject1.add_grade(4.5)
subject1.add_grade(5.0)
subject2.add_grade(3.5)


print("Student list:")
print("================")
student1.display_grades()
print("================")
student2.display_grades()


