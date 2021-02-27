"""
multi level
Person has id,name, age
Employee has id,name, age , pan , pf
Staff has id,name, age , pan , pf , contractId , contractPeriod.


Multi Level :
--------------------
 [Threee class
 Person is  a parent class
 Employee extends Person
 Staff extends Employee

Person is parent for Employee
Employee is the parent for Staff


Staff class gets the inheritence from Person and Employee.

Person has  -> id,name, age
Employee has -> id,name, age, pan, pfNo
Staff has - > id,name, age, pan, pfNo,   contactId,contarctPeriod


Person , employee , staff objs are independent.

Person  constr has  3 args
Employee constr has  5 args
Staff has  constr has  7 args


Employee constr will call person constr
Staff constr will call the employee constr

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


# Employee is child class for Person
class Employee(Person):
    def __init__(self, id, name, age, pfNo, pan):
        Person.__init__(self, id, name, age)
        self.pfNo = pfNo
        self.pan = pan

    def printEmp(self):
        print(self.pan)
        print(self.pfNo)


# Staf is child class for Employee
class Staff(Employee):
    def __init__(self, id, name, age, pan, pfNo, contactId, contarctPeriod):
        '''invoke parent constructor'''
        Employee.__init__(self, id, name, age, pan, pfNo)
        self.contactId = contactId
        self.contarctPeriod = contarctPeriod

    def displayStaff(self):
        print(self.contactId, self.contarctPeriod)


# create obj for person
print("print person info")
p = Person(2000, "user1", 56)
p.showPersonalInfo()

# create obj for employee
print("print employee info")
emp = Employee(20001, "albert", 54, "testPf", "testPan")
emp.showPersonalInfo()
emp.printEmp()

# create obj for staff
print("print staff info")
s1 = Staff(1201, "user2", 28, "proj77777", "IT", "c_88888", "12 months")
s1.showPersonalInfo()
s1.printEmp()
s1.displayStaff()