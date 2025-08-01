ds={"name":"Rithik","age":19,"friend":"sibiraj"}
print(ds)
print(ds["age"])

b=ds
b["college"]="SCET"
b["degree"]="B.TECH"
# print(b)
ds.update({"branch":"AI&DS"})
print(b)

data={"Name":"Rithik T","age":19,"native":"Salem"}
print(data)

# data.clear
# print(data)

# bio=data.copy()
# print(bio)

bio=data.items()
print(bio)

# bio=data.get("Name")
# print(bio)

# bio=data.get("bike","RS200")
# print(bio)

# bio=data.pop("native")
# print(bio)
# print(data)

# bio=data.keys()
# print(bio)

# bio=data.values()
# print(bio)
# data["game"]="FF"

# bio=ds.setdefault("native","salem")
# print(ds)

# data.update({"Bike":"RS200"})
# print(data)


#loop in Dictionaries

#key names
for i in ds:
    print(i)

    # using keys function

for i in ds.keys():
    print(i)

#values

for i in  ds:
    print(ds[i])

#using values function
for i in ds.values():
    print(i)

for i in ds.items():
    print(i)












