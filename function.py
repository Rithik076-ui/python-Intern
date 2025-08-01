def add():
    a=150
    b=250
    c=a+b
    print("addition values is",c)
add()


bal=[17000,5000,25000,65000]
def debit(money=0,pos=0):
    if money<=bal[pos]:
        bal[pos]-=money
        print(money,"debited")
        return bal[pos]
    else:
        print("can't Debit")
res=debit(16999,0)
print(res)