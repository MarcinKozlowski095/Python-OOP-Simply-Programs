class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}'

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            print(f'Added {employee}.')
        else:
            print(f'{employee} is already on the list.')

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print(f'Removed employee with ID {employee_id}.')
                return
        print(f'Employee with ID {employee_id} is not on the list.')

    def display_employees(self):
        if not self.employees:
            print('No employees to display.')
        else:
            for employee in self.employees:
                print(employee)

# Example usage
company = Company()
employee1 = Employee(1, 'Jan Nowak', 'Programista', 5000)
employee2 = Employee(2, 'Anna Nowak', 'Księgowa', 4000)

company.add_employee(employee1)
company.add_employee(employee2)

company.remove_employee(1)

company.display_employees()
