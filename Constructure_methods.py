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
print("\n")

class Voting:
    constituency = "Gundlupet"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voting(self):
        return "My name is {},age is {} and vote under {} constituency".format(self.name, self.age, self.constituency)

    @classmethod
    def my_constituency(cls):
        return "My Constituency is {}".format(cls.constituency)

    @staticmethod
    def check_age(age):
        if age>=18:
            return True
        else:
            return False
age = int(input("enter age:"))
name = input("Enter name:")
if Voting.check_age(age):
    v1 = Voting(name, age)
    print(v1.name)
    print(v1.age)
    print(v1.voting())
else:
    print("Not eligible to vote")

print("\n")

class Student:
    university = "Mysore"
    marks = []
    sum = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age= age
        self.gender = gender

    def student_details(self):
        return "My name is {}, age is {} and studying in {} university".format(self.name, self.age, self.university)

    def calculate_marks(self):
        count = 3
        for i in range(count):
            num = int(input("enter marks:"))
            self.marks.append(num)
            self.sum = self.sum + num
        return self.marks

    def avg_marks(self):
        avg = self.sum / 3
        return avg

stu1 = Student("navya" , 25, "female")
markslist1 = stu1.calculate_marks()
print(stu1.student_details()," and my marks list is" ,markslist1)
print(stu1.student_details(), "and my average marks is ", stu1.avg_marks())


