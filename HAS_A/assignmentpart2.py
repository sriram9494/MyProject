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

p1 = Person(2000,"user1",45) #Create person obj with data
a1 = Address("hosakerehalli","bangalore","560085","KA","IN")
p1.addr = a1
a2 = Address("girinagar","bangalore","560085","KA","IN")
p1.addr = a2
a3 = Address("marathalli","bangalore","67677","KA","IN")
p1.addr = a3

p1.showPersonInfo()
p1.addr.showAddressInfo()