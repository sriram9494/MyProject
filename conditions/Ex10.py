"""
take username and password as input
if username is "admin" and password is "admin" ==> print login success
if not ==> print login failure

"""
username= input("enter the username:")
password= input("enter password:")

if username =="admin":

    if password =="admin":
         print("login success")
else:
    print("login failure")
