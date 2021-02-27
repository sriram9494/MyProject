id=int(input("enter id: "))
age=int(input("enter age: "))
user=input("enter user: ")


if id>0 and age>18 and user=="admin":
    print("valid")
else:
    print("invalid")