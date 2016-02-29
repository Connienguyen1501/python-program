# Utilities

def utilities_bill(bill, money):
    if  bill > 50:
        money = bill - 50
        return money
    elif bill == 0:
        print "There is something wrong with the system!"
    else:
        print "You're fine!"
        
bill = 100
money = bill - 50
current_bill = utilities_bill(bill, money)
print current_bill

print "====="

bill = 50
money = bill - 50
current_bill = utilities_bill(bill, money)
print current_bill

print "===="

bill = 0
money = bill - 50
current_bill = utilities_bill(bill, money)
print current_bill




