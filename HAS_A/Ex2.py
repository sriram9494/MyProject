"""

Req:

capture the personinfo with address and print
capture the student info with address info and print

"""
"""
Steps:
1.Create Address class
2.Create Person class with addObj as instance variable
3.Create student class with addObj as instance variable


# for person
4.Create person obj with data
5.Create address obj with data
6.keep adress obj inside person obj
7.Print person info and address info


# for student
8.Create student obj with data
9.Create address obj with data
10.keep adress obj inside student obj
11.Print student info and address info
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



class Student:
    def __init__(self,name, clgname, semno,branch, addr=None):
        self.name = name
        self.clgname = clgname
        self.semno = semno
        self.branch = branch
        self.addr = addr

    def showStuInfo(self):
        print(self.name)
        print(self.clgname)
        print(self.semno)
        print(self.branch)

"""
class: Student
instance variables: name, clgname, semno,branch, addr   , here addr is the address object
instance function : showStuInfo()

"""


p1 = Person(2000,"user1",45) #Create person obj with data
a1 = Address("marathalli","bangalore","67677","KA","IN") #Create address obj with data
p1.addr = a1 #keep adress obj inside person obj


#display data
print("********* Show Person *************")
p1.showPersonInfo()
p1.addr.showAddressInfo()





s1=Student("mahe","siddaratha",2,"ece") #Create Student obj with data
a2= Address("t nager", "chennai", "518003", "TN", "IN") #Create address obj with data
s1.addr = a2  #keep adress obj inside Student obj



print("********* Show Student *************")
s1.showStuInfo()
s1.addr.showAddressInfo()