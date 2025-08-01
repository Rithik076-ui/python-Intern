from abc import ABC
class bus(ABC):
    def volvo(self):
        print("hello")
        print("enjoy")
class SRT(bus):
    def volvo1(self):
        print("It is a luxary bus")
class KPN(bus):
    def mahendra(self):
        print("AC bus")
class SAT(bus):
    def volvo(self):
        print("Luxary vechile")
c=SRT()
c.volvo1()
s1=SAT()
s1.volvo()
b=bus()
b.volvo()
k=KPN()
k.mahendra()

# A=ABC()
# A.volvo()

 