"""
one parent having multiple child classes.

  RBI is a parent class
  SBI , HDFC , ICICI are the child classes for RBI


RBI: Parent class has
       - createAccount()
       - processLoan()

SBI is a child of RBI
		   - demat1()

HDFC is a child of RBI
			  - demat2()

ICICI is a child of RBI
			  - demat3()


Create obj for RBI , SBI , HDFC , ICICI and call the methods.

"""


class RBI:
    def createAccount(self):
        print("RBI:: account created")

    def processLoan(self):
        print("RBI:: roi 10%")


class SBI(RBI):
    def demat1(self):
        print("SBI demat")


class HDFC(RBI):
    def demat2(self):
        print("HDFC demat")


class ICICI(RBI):
    def demat3(self):
        print("ICICI demat")


"""
How many methods in SBI?
3 [createAccount() , processLoan(), demat1() ]

How many methods in HDFC?
3 [createAccount() , processLoan(), demat2() ]

How many methods in ICICI?
3 [createAccount() , processLoan(), demat3() ]


"""

print("**********RBI**********")
rbi = RBI()
rbi.createAccount()  # LOGIC FROM RBI
rbi.processLoan()  # LOGIC FROM RBI

# create obj
print("**********SBI**********")
sbi = SBI()
sbi.createAccount()  # LOGIC FROM RBI
sbi.processLoan()  # LOGIC FROM RBI
sbi.demat1()  # LOGIC FROM SBI

print("**********HDFC**********")
h = HDFC()
h.createAccount()  # LOGIC FROM RBI
h.processLoan()  # LOGIC FROM RBI
h.demat2()  # LOGIC FROM HDFC

print("**********ICICI**********")
i = ICICI()
i.createAccount()  # LOGIC FROM RBI
i.processLoan()  # LOGIC FROM RBI
i.demat3()  # LOGIC FROM ICICi