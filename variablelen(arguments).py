#variable length arguments
# variable len arguments are automaticatically stored in tuple and we use star arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"gopi","age":22,"place":"vij"}
check(*d)'''

'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d+=i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"pythnpy")'''


#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"name":["gopi","arjun","mahesh"],
       "marks":[60,70,80],
       "status":["p","A","p"]}
check2(**details)'''


#both  * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d+=i
        print(d)
    for i,j in b.items():
        print(i,j)
final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"name":["gopi","arjun","mahesh"],
       "marks":[60,70,80],
       "status":["p","A","p"]}
final(**details)
final(*data,**details) '''



#Task Railway ticket
def Railway():
    ticket_price = 1000

    Gender = input("""Enter your Gender:
1. male
2. female
""").lower()

    if Gender == "male" or Gender == "female":
        age = int(input("Enter your age: "))

        if Gender == "male" and age > 60:
            print("You are eligible for 30% off")
            senior_price1 = ticket_price - (ticket_price * 30 / 100)
            print(senior_price1)

        elif Gender == "female" and age > 60:
            print("You are eligible for 500/- off")
            senior_price2 = ticket_price - 500
            print(senior_price2)

        elif Gender == "female":
            print("You are eligible for 700/- off")
            price1 = ticket_price - 700
            print(price1)

        else:
            print("You are not eligible for discount!")
            print(ticket_price)

    else:
        print("Invalid Gender")


while True:
    Railway()
