class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)

class Child(Parent):
    pass
child = Child("Navya", "shree")
child.print_name()
print("\n")

class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def eat(self):
        super().eat()
        print("I like to eat bones")
dog = Dog()
dog.name = "Charli"
print(dog.name)
dog.eat()
print("\n")
class Cat(Animal):
    def eat(self):
        super().eat()
        print("I like to drink milk")
cat = Cat()
cat.name = "billi"
print(cat.name)
cat.eat()

# single level inheritance
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
class Triangle(Polygon):
    pass

tri = Triangle([5, 6, 8])
print("Perimeter of traingle is ",tri.perimeter())
print("\n")

class University:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return "This is {} university".format(self.name)

class College(University):
    def __init__(self, name, college_name):
        super().__init__(name)
        self.college_name = college_name

    def get_info(self):
        return "This is {} college, part of {} university".format(self.college_name, self.name)

class Student(College):
    def __init__(self, name, college_name, student_name):
        super().__init__(name, college_name)
        self.student_name = student_name

    def get_info(self):
        return "This is {}, student at {} which is a part of {} university".format(self.student_name, self.college_name, self.name)

stu = Student("VTU", "Maharaja institute of technology", "Navya")
print(stu.get_info())

# Multiple inheritance
class Mammal:
    def give_birth(self):
        print("Giving birth to young ones")
class FlyingCreature:
    def fly(self):
        print("Flying in sky")
class Bat(Mammal,FlyingCreature):
    def __init__(self, name):
        self.name = name
bat = Bat("Fruitbat")
print("Bat's name:",bat.name)
bat.give_birth()
bat.fly()












