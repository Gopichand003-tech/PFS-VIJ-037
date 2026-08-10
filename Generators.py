# Generators - > No tuple comprehension in above cases if we remove those braces and keep paranthesis when out come is generator

#[expr for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

#(expr for var in collection/range)
#a=(i for in range(16))
'''print(a)
print(*a)
print(types(a))'''

'''b=list(a)
print(b)

print(tuple(a))
print(set(a))'''

#definition -> a generator is also a function which can be used as an iterator (loops) by producing group of values , where we can yeild keyword.

#yeild vs return
# return will terminate the function where as yeild can pass the function and go on with every success iteration.

'''a,b=[int(x) for x in input("Enter the values: ").split(",")]
def check(a,b):
    while a<b:
         yield a
         a += 1
         yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("Enter the values: ").split(",")]
def check(a,b):
    while a<b:
         a += 1
         #return a
    return a
print(check(a,b))'''

'''def mygen():
    #return "vij"
    #return "hyd"
    #return "vzg"
    return "via","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())'''

#next()
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))'''
# print(next(d)) stop iteration

n=5
for i in range(1,n):
     print(" " *(n-i-1)+ "*" * )

         
