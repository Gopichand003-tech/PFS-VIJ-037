''' diff btw break , continue , pass

1.break is used to terminate the entire loop.
2.continue statement is used to skip the current iteration and rest of the code will continue.
3.A pass is null statement it does nothing but sytatical we need.'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==13:
        break
    print(i)'''

'''a="python"
if a=="h": 
    break
print(a)''' #error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=20
while a>5:
      print(a)
      a=a-1
      if a==10:
      continue'''

'''for i in range(15):
       if i==7:
           continue
        print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass
'''a=30
while a>10:
     print(a)
     a=a-1
     if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''

#Task

Account = 100000
card = 'c'
pwd = "1234"

insert_card = input("Insert the card:")
if insert_card == 'c':
    print("Welcome Gopichand")
else:
    print("Invalid Card")
    
#password
password = input("Enter Password :")
if password == pwd:
    option = int(input("Select an option"))
    if option == 1:
        print("Balance Account")
    elif option == 2:
            print("With Draw")
    else:
        print("No account")
else:
    print("Invalid Password!")

#withDraw
amount = int(input("Enter Amount : "))
amount -= Account
print(f"Cash Debited successful")


#checkbalance
select = input("Check balance:")
if select == '1':
     balance = (Account - amount)
print(f"your balance : {balance}")
