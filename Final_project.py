class account:
    def __init__(self, acc_number, acc_holder):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = 0.0
class Transaction(account):
    def operation(self, amount):
        self.balance += amount
        print(f"your amount {amount} Deposit successfully.")

class deposit(Transaction):
    def operation(self, amount, action):
        if action == "deposit":
            super().operation(amount)
        elif action == "Withdrawl":
            if amount > self.balance:
                print("!Insufficient balance")
            else:
                self.balance -= amount
                print(f"your Amount {amount} Withdrawl successfully.")
while True:
    acc_number=input("Enter your 15 digit Account Number:")
    if acc_number.isdigit() and len(acc_number)==15:
        print("Account Number is valid")
        break
    else:
        print("!Try again your Account Number must be 15 digits")
        print("HEllo")
    
acc_holder=input("Enter Your Account Holder's Name: ")
print("\n[----------WELCOME TO SBI BANK----------]")
ac=deposit(acc_number,acc_holder)
while True:
    print("\n Choose an option: ")
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Balance Enquiry")
    print("4. Exit")

    ans= input("Enter your choice [1-4]: ")
    if ans=="1":
        amt=float(input("Enter your Deposit amount: "))
        ac.operation(amt,"deposit")
    elif ans=="2":
        amt= float(input("Enter Your Withdrawl amount: "))
        ac.operation(amt,"Withdrawl")
    elif ans=="3":
        print(f"Current Balance: {ac.balance}")
    elif ans=="4":
        print(f"\n!Thankyou Visit Again {acc_holder},Logging out from Your Account {acc_number}.")
        break
    else:
        print("!Invalid choice.please select between 1 and 4.")