#calender module

'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

#year
'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#Date & Time
'''import datetime
a=datetime.datetime.now()
print(a)'''

'''from datetime import date
a=date.today()
print(a)'''

'''import time
a=time.time()
#print(a)
b=time.localtime(a)
print(b)
# time.struct_time(tm_year=2026, tm_mon=7, tm_mday=28, tm_hour=12, tm_min=5, tm_sec=43, tm_wday=1, tm_yday=209, tm_isdst=0)

print(f"Now the time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
#Now the time is 12-5-43

print(f"week of the day is {b.tm_wday} and year of the day is {b.tm_yday}")
#week of the day is 1 and year of the day is 209'''

'''import random
import time
for i in range(10):
    a=random.randint(1,10)
    time.sleep(2)
    print(a)'''

'''error handling
syntax error -> compile error
run_time error -> during excecution time it will happens
logical error -> error in ligic(in cant visible)'''

#syntax error
'''for i in range(10)
print(i)'''

#run time error
'''a=int(input())
b=int(input())
print(a//b)''' # 10/10 -> zero division error

#logical error
'''a=10
b=20
print(a-b)'''


