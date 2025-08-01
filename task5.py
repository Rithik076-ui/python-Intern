class bank:
    def account(self, accnumb, holedername):
        self.accnumb=accnumb
        self.holdername=holedername
        self.balance=1000
class withdrawl(bank):
    def interface(self):
        holdername=input("enter your accname")
    accnumb="09530100019519"  
    while accnumb<=15:
      accnumb=int(input("enter your acc numb"))
    if accnumb>=15:
        print()
    else:
        print("invaild account number")
        self.account(accnumb,holdername)


    def amount1(self):
        amount=float(input("enter your Deposit amount"))
        if amount >0:
            self.balance+=amount
            print("your amount is deposited sucessfully")
        else:
            print("your amount is invaild! please give vaild amount")
        
            


    def calculate_interest(self):
        rate = float(input("Enter annual interest rate: "))
        time = float(input("Enter time period: "))
        interest = (self.balance * rate * time) / 100
        print(f" Interest earned: RS{interest}")
        print(f"Total balance after interest: {self.balance + interest}")

class final(withdrawl):
    def get_balance(self):
        print("------account details------")
        print(f"account holder:{self.holdername}")
        print(f"accountnumb:{self.accnumb}")
        print(f"current balance:${self.balance}")
        print("Thankyou for Visiting us")
c=final()
c.interface()
c.amount1()
c.calculate_interest()
c.get_balance()










        



        
