"""
take cityname as input

if cityname is "chennai" or "bangalore" or "hyd" or "mumbai"  o/p:====> service provided
for any other city ====> servcie not provided

"""
cityname=["chennai","bangalore","hyderabad","mumbai"]
city=input("enter the city name")

if city in cityname:
    print("service provided")
else:
    print("service not provided")