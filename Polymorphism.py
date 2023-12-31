# It is the behaviour of method when different objects acts upon it
# Polymorphism using Inheritance
class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
print("\n")

# Polymorphism using classes and methods
class India:
    def capital(self):
        print("New Dehli is the capital of India")

    def language(self):
        print("Hindi is the most widely language spoken language of India")

    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("Washington is the capital of USA")

    def language(self):
        print("English is the most widely language spoken language in USA")

    def type(self):
        print("USA is a developed country")

obj_india = India()
obj_Usa = USA()

for country in (obj_india, obj_Usa):
    country.capital()
    country.language()
    country.type()
print("\n")

# polymorphism using function and object
class India:
    def capital(self):
        print("New Dehli is the capital of India")

    def language(self):
        print("Hindi is the most widely language spoken language of India")

    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("Washington is the capital of USA")

    def language(self):
        print("English is the most widely language spoken language in USA")

    def type(self):
        print("USA is a developed country")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_india = India()
obj_Usa = USA()

func(obj_india)
func(obj_Usa)






