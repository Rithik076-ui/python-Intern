class sam:
    def name(self):
        print("sampk")
class raja(sam):
    def name(self):
        super().name()
        print("raja")
class arun(raja):
    def name(self):
        super().name()
        print("ARUN")
s=arun()
s.name()
# s.name()
# s.name()
# s1=raja()
# s1.name()


# 🏦 Basic Banking Console Application with Account Number Validation

def show_menu():
    print("\n--- Welcome to MiniBank ---")
    print("1. Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Balance Enquiry")
    print("4. Exit")

def deposit(balance):
    amount = float(input("Enter amount to deposit: ₹ "))
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: ₹ "))
    if amount > balance:
        print("Insufficient balance! 🛑")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    return balance

def balance_enquiry(balance):
    print(f"Current Balance: ₹{balance:.2f}")

# 🧑 Account Setup with Validation
while True:
    acc_number = input("Enter your 15-digit Account Number: ")
    if acc_number.isdigit() and len(acc_number) == 15:
        break
    else:
        print("❌ Invalid account number. Please enter exactly 15 digits.")

acc_holder = input("Enter Account Holder's Name: ")
balance = 0.0

# 🌀 Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        balance = deposit(balance)
    elif choice == '2':
        balance = withdraw(balance)
    elif choice == '3':
        balance_enquiry(balance)
    elif choice == '4':
        print(f"\nThank you, {acc_holder}! Your account ({acc_number}) is now safely logged out. 👋")
        break
    else:
        print("Invalid choice. Please enter 1 to 4.")
