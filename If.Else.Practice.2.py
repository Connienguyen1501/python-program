# Biking

def greet(friend, bike):
    if friend and bike:
        print "Hi! Let's bike together"
    elif friend:
        print "Hi! Do you like biking?"
    else:
        print "Hello!"
        
friend = "Bob"
bike = True
friend = greet(True, bike)

friend = "Dave"
bike = False
friend = greet(True, bike)

friend = "Ryan"
bike = False
friend = greet(False, bike)
