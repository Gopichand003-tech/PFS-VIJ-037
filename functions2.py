'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
      a=int(input())
      b=int(input())
      option=int(input(''Select the option 1.add 2.sub 3.mul''))
      if option == 1:
          add()
      elif option == 2:
           sub()
      elif option == 3:
           mul()
      else:
          print("Choose the correct option")'''


#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="gopi"
    mailid="gopichand@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="manoj",mailid="m@gmail.com")
Details(id=30,name="sai",mailid="s@gmail.com")
Details(40,"Trinadh","t@gmail.com")
Details("v@gmail.com",50,"vijay")
Details(mailid="g@gmail.com",id=60,name="gopi")'''

#default arguments
'''def grocery(items,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("sugar",100)'''

'''def grocery(items="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(items,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dal")'''

#cakes
'''def cakes(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cakes("Redvelvet",80,2)

def cakes(cake_name="chocolate",price=80,qty=4):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cakes()

def cakes(cake_name="vanila",price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cakes(80,2)

def cakes(cake_name,price=60,qty=3):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cakes("pineapple")'''


# * arguments(* is used to unpack the elements)
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''

'''a={2,3,4,5,6,7}
print(a)
print(*a)'''

'''b={"name":"gopi","city":"vij"}
print(b)
print(*b)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#Error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

''' *a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)''' #Error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

