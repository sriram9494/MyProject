class Person:

    # constructr logic start
    def __init__(self, pId, pName, pAge):
        print("constr called")
        self.id = pId
        self.name = pName
        self.age = pAge



# Create object

p1 = Person(2000, "kumar", 34)  # obj is created , internally calls _init_

p2 = Person(2001, "ram", 38)  # obj is created , internally calls _init_

p3 = Person(2003, "raj", 39)  # obj is created , internally calls _init_


print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)
print(p3.id,p3.name,p3.age)