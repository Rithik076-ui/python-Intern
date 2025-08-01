ds={"Rithik","kavin","santhosh","sibiraj","pavithra","a","pavithra"}
print(ds)
print(type(ds))
print(len(ds))

k=set(("Rithik","kavin","santhosh","pavithra"))
print(ds)

p={"Rithik","kavin","santhosh","pavithra"}
k1={"velvizhi"}
p.update("pooja")
print(k1)

a=ds
li=["b"]
a.update(li)
print(a)

a.remove("a")
print(a)

a.discard("b")
print(a)


# b=ds.pop()
# print(b)
# print(ds)

for i in ds:
    print(i)

print("Rithik" in ds)

