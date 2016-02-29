# Give 20 bucks 

def greet(friend, money):
    if friend and (money >= 20):
        print "Hi! Here is my money"
        money = money - 20
    elif friend:
        print "Hi! I don't have any money for you"
    else:
        print "Give me your money!"
    return money

money = 25

money = greet(True, money)
print "Money:", money

print "====="

money = 15

money = greet(True, money)
print "Money:", money

print "===="

money = 50

money = greet(False, money)
print "Money:", money