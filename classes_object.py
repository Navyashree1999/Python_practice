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



