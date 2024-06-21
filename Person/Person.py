"""
Zadanie 6: Klasa Person i Employee
Stwórz klasę Person, która przechowuje imię, nazwisko i wiek.
Następnie stwórz klasę Employee, która dziedziczy z Person i
dodatkowo przechowuje informacje o wynagrodzeniu oraz stanowisku.
Dodaj metody do wyświetlania tych informacji.
"""

class Person:
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, first_name, last_name, age, salary, position):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.position = position

    def display(self):
        super().display()
        print(f"Salary: {self.salary}, Position: {self.position}")


person = Person('Joe', 'Doe', 20)
employee = Employee('Joe', 'Doe', 20, 5000, 'Data Analyst')

person.display()
print('-' * 10)
employee.display()
