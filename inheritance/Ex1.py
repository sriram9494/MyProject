"""
Req:
Person has id, name, age as instance variables
Employee has id, name, age, pan, pfNo as instance variables

create obj and set data for person and employee.

w/o inheritence
------------------------------------------
class Person:
     id=None
     name=None
     age=None

    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)


class Employee :
    pan= None
    pfNo=None
    id=None
    name=None
    age=None

    def printEmp(self):
        print(self.pan)
        print(self.pfNo)
        print(self.id)
        print(self.name)
        print(self.age)

"""


class Person:
    id = None
    name = None
    age = None

    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)


# Employee class as child
class Employee(Person):
    pan = None
    pfNo = None

    def printEmp(self):
        print(self.pan)
        print(self.pfNo)


# emp class is reusing id,name,age and showPersonalInfo() funtn

# create obj ; set data and show
print("print person info")
p = Person()
p.id = 2000
p.name = "user1"
p.age = 34

p.showPersonalInfo()  # shows id,name, age for person

print("print employee info")
emp = Employee()
emp.id = 4000
emp.name = "user2"
emp.age = 39
emp.pan = "testpan"
emp.pfNo = "testpf"

emp.showPersonalInfo()  # shows id,name, age for emp
emp.printEmp()  # show pan, pfNo of emp

# emp obj is reusing id,name,age and showPersonalInfo() funtn
# showPersonalInfo()  can be called by parent obj and child obj