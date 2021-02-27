"""
take bankname as input

if bankname is "sbi" , o/p: 10%
if bankname is "hdfc" , o/p: 11%
if bankname is "icici" , o/p: 12%
if bankname is "citi" , o/p: 13%
for any other bank , o/p: invalid bank
"""

bankname= input("enter the bankname")
bank= {
    "sbi":"10%",
    "hdfc":"11%",
    "icici":"12%",
    "citi":"13%"
}
if bankname.key():
    print(bank(bankname))

#if
