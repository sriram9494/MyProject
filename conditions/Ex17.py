"""
take username and password as input
if username is "admin" and password is "admin" ==> print login success
if not ==> print login failure

"""


username, password = input("enter two values").split()

if (username == "admin" and password == "admin"):
    print("login is successful")
else:
    print("login is failed")