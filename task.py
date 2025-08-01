# Annual_income=1200000 ##salary Package 
# House_rent=240000
# provident_fund=72000 ## house rent per annum
# gratutity=23000 ##gratutity per annum
# income_tax=500*12 ##500 per month
# food=5000*12 ## 500 per month
# speical_allowances=Annual_income-(House_rent+gratutity+food) ## calculating speical allowances
# total_detuction=House_rent+provident_fund+gratutity+food+income_tax ## Total Deduction
# Take_Home_Salary_per_annum=Annual_income-total_detuction ##calculating annual salary
# Take_Home_Salary_per_month=Take_Home_Salary_per_annum/12 ## calculating monthy salary
# print("Your Take home Salary is:",Take_Home_Salary_per_annum)
# print("your monthly Salary is:",Take_Home_Salary_per_month)





#Black Thunder

age=int(input("Enter your age:"))
if (age>=5 and age<=60):
    print("----------wecome To Black Thunder----------")
    print("------Enjoy your day in Black Thunder-----")
    age=int(input("Enter your age:"))
    height=int(input("Enter your Feet:"))
if(age>=10 and age<=50):
    if(height>=3 and height<=7):
        print("Welcome to Roller coaster Ride")
    else:
         print("Please visit your Height category games")
elif (age>=5 and age<10):
    print("!Sorry You are Not Allowed to Roller Coaster")
    print("--------Please visit Kids Game--------")
elif (age>50 and age<=60):
        print("!Please vist your Age category games")
else:
    print("--------Thankyou! visit again--------")

# def city(name, favourite_city):
#     print(f"Hello {name}, let's talk about your favourite city!")
#     ans = input("Enter your favourite city: ")

#     if ans == "salem":
#         print("Salem is known for its vibrant culture and steel production.")
#     elif ans == "ooty":
#         print("Ooty is a serene hill station with beautiful views.")
#     elif ans == "kashmir":
#         print("Kashmir is a stunning destination often called 'Paradise on Earth'.")
#     else:
#         print("Wherever you go, may it bring joy and peace!")
# city("Rihtik","salem")       






def city(name,favourite_city):
    print(f"hello{name},is your favorite city is{favourite_city}?")
    ans=input("Type Yes or No:")
    if ans=="no":
        favourite_city=input("enter the favourite city:")
    if favourite_city=="salem":
        print("Salem is known for mangoes and steel production.")
    elif favourite_city=="ooty":
        print("Ooty is a peaceful hill station in Tamil Nadu.")
    elif favourite_city=="kashmir":
        print("Kashmir is breathtaking with snowy mountains and valleys.")
    else:
        print("where ever you go,Enjoy it!")
city("Rithik",'Salem')




# seats=1
# while seats<=100:
#     amt=int(input("tell us amount"))
#     if amt>=190:
#         print("ticket bokked @",seats)
#         seats+=2
#     else:
#         print("Insufficient Balance")







# list task

data=["Rithik","kavin",7.5,19,619]
print(data)

#append in list
data.append("santhosh")
print(data)

#insert in list
data.insert(2,"vasanth")
print(data)

#insert the element in particular place in list
data[6]=4
print(data)

#print max and min value in the list
data1=[3019,90,245,717,90,66,456,90,90]
print(min(data1))
print(max(data1))

#summation in the list
print(sum(data1))
print(data1.reverse())
print(data1)

#pop element in the list
print(data.pop(2))
print(data1.pop(3))
print(data1)
print(data)

# copy method  in list
star=data1.copy()
print("copy of rk:",star)

#count operation in the list
star=data1.count(90)
print(star)

#list user

z=(input("enter the name"))
li=z.split(",")
print("list names")
for i in li:
    print(i)

# looping list

loo=int(input("enter the list:"))
li1=[]
for i in range(5):
    list=input("enter the list:")
    li1.append(list)
print("list nmuber is",li1)


#middle list

a=data1
print("orginal list is:",a)
loop=int(input("enter the number :"))
insert=int(input("enter the position:"))
a.insert(insert,loop)
print("added list is:",a)






















