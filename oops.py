class car:
    def __init__(self,brand ,name):
        self.brand=brand
        self.name=name
    def display(self):
        print(f"brand:{self.brand},name:{self.name}")
c=car("BMW","f1")
c1=car("audi","c class")
c.display()
c1.display()

# single inheritance
class bike:
    def gear(self):
        print("5 speed gear box")
class car(bike):
    def benz(self):
        print("is the classic car")
c=car()
c.benz()
c.gear()

