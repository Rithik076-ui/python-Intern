# class sam:
#     def sa(self,a):
#         print(a)
#     def sa(self,a,b):
#         print(a+b)
#     def sa(self,a,b,c):
#         print(a+b+c)
# s=sum()
# s.sa(10,20,250)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# c=over()
# print("sum",c.load(10))
# print("sum",c.load(10,20))
# print("sum2",c.load(10,20,30))



class rithik:
    def name(self):
        print("Rithik star")
class raja(rithik):
    def name(self):
        super().name()
        print("raja")
class arun(raja):
    def name(self):
        super().name()
        print("arun")
a=arun()
a.name()


