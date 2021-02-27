id = int(input("enter user id "))
age = int(input("enter user age"))
type = input("enter user type")



#approach1 Using and
if (id>0  and age>18 and type== 'admin' ):
    print("Valid data")
else:
    print("Invalid data")