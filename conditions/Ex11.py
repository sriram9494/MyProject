"""
take id ,age , usertype as input
perform validation

id should be positive:
age should be greater than 18:
usertype should be "admin":

if id,age,usertype is valid ==> print valid data
if any data found to be invalid ==> print invalid data

 """

id=int(input("enter id: "))
age=int(input("enter age: "))
user=input("enter user: ")

if id>0:
    if age>18:
        if user=="user":
            print("valid data=",id,age,user)
else:
    print("invalid data=",id,age,user)
