# anonymous function(nameless functions)
# definition -> anonymous functions are name less functions and we use a keyword called 'lambda' to create anonymous functions

'''def f(x):
    return 2*x+5
print(f(5))'''

'''def f():
    x=int(input("value: "))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a=int(input("a valiue: "))
b=int(input("b value: "))
c=lambda a,b:a*b
print(c(a,b))'''

'''x=input()
y = lambda x:x.upper()
print(y(x))'''

'''x=input()
y=lambda x:x.title()
print(y(x))'''

'''x=input()
y=input()
z=lambda x,y:(x+" "+y).title()
print(z(x,y))'''

'''a,b=[x for x in input().split(",")]
c=a+" "+b
d=lambda a,b:c.title()
print(d(a,b))'''

#filter
'''a=[10,30,50,100,127,39,45,67,200]
b=list(filter(lambda i:i % 2 == 0,a))
print(b)'''


'''a=[[],(),set(),{}," ",None,5,8.9,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''
