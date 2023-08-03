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


