"""
take id ,age , usertype as input
perform validation

id should be positive:
age should be greater than 18:
usertype should be "admin":

if id,age,usertype is valid ==> print valid data
if any data found to be invalid ==> print invalid data

 """

id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")


if id >0 :
   if (age > 18):
       if (usertype == "admin"):
            print("valid usertype") # three tabs here
       else:
            print("invalid Data")# three tabs here
   else:
        print("invalid Data") # two tabs here
else:
    print("invalid Data")