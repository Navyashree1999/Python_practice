class Employee:
    def __init__(self, emp_id, first_name, last_name, salary, role):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.role = role

    def employee_name(self):
        return "employee firstname is {} and lastname is {}".format(self.first_name, self.last_name)

    def employee_details(self, name):
        return "My name {} and i am working as {}".format(name, self.role)

employee1 = Employee(20, "Navya", "shree", "25k", "developer")
print(employee1.employee_name())
print(employee1.employee_details("Navyashree"))
print("\n")

employee2 = Employee(21, "Divya", "shree", "30k", "developer")
print(employee2.employee_name())
print(employee2.employee_details("Divyashree"))
