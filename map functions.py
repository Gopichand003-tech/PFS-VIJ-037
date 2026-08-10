#map() -> Each object from collection and forms a new collection

#max
'print(max(4,5,7,8,10,20))'

#min
'print(min(4,5,7,8,10,20))'

#sum
'''a=1,23,4,5
print(sum(a))'''

'''a=[2,5,7,8,10,12,14,16,20,25,30]
b=[1,3,5,7,9,11,15,17,21,24,30]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''

'''a=[2,5,7,8,10,12,14,16,20,25,30]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''

'''a=[2,5,7,8,10,12,14,16,20,25]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the names").split(",")
print(a+b)'''

'''a,b=[x for x in input("names").split(",")]
print(a+b)'''

'''a,b=map(str,input("enter,the names").split(","))
print(a+b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''a,b=[int(x) for x in input().split(",")]
print(a+b)'''

'''a,b=int(input()).split(",")
print(a+b)''' #error

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

''''a=list(map(int,input("Enter the values").split(","))
print(a)
print(type(a))

a=tuple(map(int,input("Enter the values").split(","))
print(a)
print(type(a))'''

'''a=input("enter the key value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''


#task

'''n=int(input("Enter number of students: "))
mark=[]
for i in range(1,n+1):
    marks=float(input(f"enter the marks for {i}"))
    mark.append(marks)
print("Total students",n)
c=max(mark)
print("heighest marks",c)
low=min(mark)
print("lowest",low)
total=sum(mark)
print("total",total)
average= (total/n) 
print("average",average)'''








