#input
id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")

if id <0 :
    print("invalid id")
elif (age < 18):
    print("valid id")
    print("invalid age")
elif (usertype != "admin"):
    print("valid id")
    print("valid age")
    print("invalid usertype")
else:
    print("valid id")
    print("valid age")
    print("valid usertype")