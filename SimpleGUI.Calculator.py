# Import simplegui


import simplegui
import math


# Define global variables (program state)
store = 12
operand = 3


# Define "Helper" functions

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def sqr():
    """square store and operand"""
    global store, operand
    store = math.sqrt(store)
    operand = math.sqrt(operand)
    output()

def fact():
    """ sfactorial of store and operand"""
    global store, operand
    store = math.factorial(store)
    operand = math.factorial(operand)
    print store, operand

# Create frame
frame = simplegui.create_frame("Calculator",200,200)

# Register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_button("Square", sqr, 100)
frame.add_button("Factorial", fact, 100)

#Start frame
frame.start()