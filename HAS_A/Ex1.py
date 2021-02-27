"""

Req: capture the personinfo with address and print


Steps:
1.Create Address class
2.Create Person class with addObj as instance variable

3.Create person obj with data
4.Create address obj with data
5.keep adress obj inside person obj
6.Print person info and address info


"""


class Address:
    def __init__(self, street, city, pin, state, country):
        self.street = street
        self.city = city
        self.pin = pin
        self.state = state
        self.country = country

    def showAddressInfo(self):
        print(self.street)
        print(self.city)
        print(self.pin)
        print(self.country)
        print(self.state)


"""
class: Address
instance variables: street, city, pin, state,country
instance function : showAddressInfo()
"""


class Person:
    def __init__(self, id, name, age, addr=None):
        self.id = id
        self.name = name
        self.age = age
        self.addr = addr

    def showPersonInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)



"""
class: Person
instance variables: id,name,age,addr   , here addr is the address object
instance function : showPersonInfo()

"""


#Create person obj with data
p1 = Person(2000,"user1",45)

#Create address obj with data
a1 = Address("marathalli","bangalore","67677","KA","IN")


#keep adress obj inside person obj
p1.addr = a1

#display data
print("**********approach1**************")
print(p1.id)
print(p1.name)
print(p1.age)

print(p1.addr.street)
print(p1.addr.city)
print(p1.addr.country)
print(p1.addr.state)
print(p1.addr.pin)


print("**********approach2**************")
p1.showPersonInfo()
p1.addr.showAddressInfo()