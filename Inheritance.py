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



