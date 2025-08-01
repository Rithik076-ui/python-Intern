saiyan=["rithik",9.0,67,"hi"]
print(saiyan)
saiyan.append("Data scientist") # append is used to add the element  in the last in the list
print(len(saiyan))
print(saiyan)
saiyan.insert(7,100) # insert any element in any position
print(saiyan)
saiyan[4]="Team lead" # replace the value in the list
print(saiyan)
shirt=[7000,8000,13000,3000,25000,10]
print(min(shirt))
shirt.remove(3000)
print(shirt)
print(shirt.pop()) # pop up the whole list
print(shirt.pop(1)) #pop up the  particular element 
print(shirt.reverse())
print(shirt)



#list methods
Rk=[1,7,6,9,0,0,0,0,3,4]
a=Rk.copy()
print("cpy:",a)
count=a.count(0)
print(count)


#list user input
rk=input("enter your Name")
list=rk.split(".")
print("list names")
for i in list:
    print(i)


n=int(input("enter the list"))
list1=[]
for i in range(5):
    lival=input("enter the list:")
    list1.append(lival)
print(list1)

