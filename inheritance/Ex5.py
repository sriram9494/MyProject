"""
RBI is a parent class
SBI , HDFC , ICICI are the child classes for RBI

RBI: Parent class has
       - createAccount()
       - processLoan()   -> roi 10%

HDFC :---> roi 10 % is fine on top of that HDFC would like to charge Rs.2000.
          Roi 10% should come from RBI and additional charge 2000 should come from HDFC.


solution :
overriding + call parent method from child
"""


class RBI:
    def createAccount(self):
        print("RBI:: account created")

    def processLoan(self):
        print("RBI:: roi 10%")


class SBI(RBI):
    def demat(self):
        print("SBI demat")


class ICICI(RBI):
    def demat(self):
        print("ICICI demat")


class HDFC(RBI):
    def demat(self):
        print("HDFC demat")

    def processLoan(self):
        RBI.processLoan(self)  # call parent method from child
        print("HDFC rs .2000 charge")


# create obj
print("**********SBI**********")
sbi = SBI()
sbi.createAccount()  # LOGIC FROM RBI
sbi.processLoan()  # LOGIC FROM RBI
sbi.demat()  # LOGIC FROM SBI

print("**********ICICI**********")
i = ICICI()
i.createAccount()  # LOGIC FROM RBI
i.processLoan()  # LOGIC FROM RBI
i.demat()  # LOGIC FROM ICICI

print("**********HDFC**********")
h = HDFC()
h.createAccount()# LOGIC FROM RBI
h.processLoan()# LOGIC FROM HDFC + RBI
h.demat() # LOGIC FROM HDFC7 ``             `