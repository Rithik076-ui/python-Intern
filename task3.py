ds=("Rithik","kavin","santhosh","sibiraj","pavithra","a")
print(ds)
print(type(ds))

print(ds[0:4])
print(ds[:3])
print(ds[4:])

a1=(89,99,0,0,7,7,6,6,5467,3019)
b1=a1.count(6)
print(b1)


#index

c1=a1.index(7)
print(c1)

#append 

d1=list(ds)
d1.append("velvizhi")
d1=tuple(d1)
print(d1)

#adding tuple in tuple
a=ds
b=("priya dharshini",)
a+=b
print(a)

if "pavithra" in ds:
    print("Cute")
else:
    print("not in ds")
a1=ds
del a
print(a1)

b=list(ds)
b.remove("a")
ds=tuple(b)
print(b)