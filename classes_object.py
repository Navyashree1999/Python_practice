class Laptop:
    name = 'Dell'
    model = "Dell Vostro"
    processer = "Intel i5"

    def power_on(self):
        print(f"{self.name} {self.model} is powering on")

    def power_of(self):
        print(f"{self.name} {self.model} is powering of")

laptop1 = Laptop()
print(laptop1.name)
print(laptop1.model)
print(laptop1.processer)
laptop1.power_on()
laptop1.power_of()
print("\n")

class Telivision:
    brand = "Sony"
    model = "Bravia 4k"
    screen_size = 55
    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off")

tv = Telivision()
print(tv.brand)
print(tv.model)
print(tv.screen_size)
tv.turn_on()
tv.turn_off()
print("\n")

class Employee:
    emp_id = 2327290
    name = 'Navya'
    department = "IT"
    email = "navyashree@gmail.com"
    phone_no = 5647834946

    def work_as(self):
        print(f"{self.name} works as system engineer")

    def leave(self,date):
        print(f"{self.name} is appling leave on {date}")
emp = Employee()
print(emp.emp_id)
print(emp.name)
print(emp.email)
print(emp.phone_no)
print(emp.department)
emp.work_as()
emp.leave(25)
print("\n")

class Pen:
    brand = "Cello"
    colour = "blue"

    def write(self):
        print(f"write using {self.brand} {self.colour} link pen")
pen = Pen()
print(pen.brand)
print(pen.colour)
pen.write()




