"""

Person has id, name, age as instance variables
Employee has id, name, age, pan, pfNo as instance variables

create obj and set data for person and employee.

#__init__ is the constructor we need to write for Person and Employee.

#Person constr HAS 3 args
#Employee constr has 5 args
#From Employee constr we need to call the person constr
"""


class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)


# Employee class as child
class Employee(Person):
    def __init__(self, id, name, age, pfNo, pan):
        Person.__init__(self, id, name, age)
        # calling parent constr from child constr
        # reuse the initializn logic for id,name,age
        self.pfNo = pfNo
        self.pan = pan

    def printEmp(self):
        print(self.pan)
        print(self.pfNo)


# create obj for person
print("print person info")
p = Person(2000, "user1", 56)
p.showPersonalInfo()

# create obj for employee
print("print employee info")
emp = Employee(20001, "albert", 54, "testPf", "testPan")
emp.showPersonalInfo()
emp.printEmp()