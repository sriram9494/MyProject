id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")


if id >0 :
    print("valid id")
    if (age > 18):
        print("valid age") # two tabs here
        if (usertype == "admin"):
            print("valid usertype") # three tabs here
        else:
            print("invalid usertype")# three tabs here
    else:
        print("invalid age") # two tabs here
else:
    print("invalid id")