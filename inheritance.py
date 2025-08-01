# single inheritance

class Dog:
    def barking(self):
        print("Dog barking high")
class cat(Dog):
    def memow(self):
        print("Memow the cat")
c=cat()
c.barking()
c.memow()        

#multilevel inheritance
class eagle:
    def speed(self):
        print("eagle eating the snake")
class snake1(eagle):
    def poison1(self):
        print("snake eating the frog")
class snake2(snake1):
    def poison2(self):
        print("frog eating the insects")
c=snake2()
c.speed()
c.poison1()
c.poison2()


#multiple inheritance
class eagle:
    def speed(self):
        print("eagle eating the snake")
class snake:
    def venom(self):
        print("snake eating the frog")
class fooodchain(eagle,snake):
    def frog(self):
        print("this is food chain")
rk=fooodchain()
rk.speed()
rk.venom()
rk.frog()

#heirarchical inheritance
class eagle:
    def speed(self):
        print("eagle eating the snake")
class snake(eagle):
    def venom(self):
        print("snake eating the frog")
class frog(eagle):
    def poison(self):
        print("frog eating the insects")
class fooodchain(frog,snake,eagle):
    def insects(self):
        print("this is food chain")
rk=fooodchain()
rk.speed()
rk.venom()
rk.poison()
rk.insects()


#hybrid inheritanace
class eagle:
    def speed(self):
        print("eagle eating the snake")
class snake(eagle):
    def venom(self):
        print("snake eating the frog")
class frog(eagle):
    def poison(self):
        print("frog eating the insects")
class fooodchain(snake,eagle):
    def insects(self):
        print("this is food chain")
rk=fooodchain()
rk.speed()
rk.venom()
rk.insects()



