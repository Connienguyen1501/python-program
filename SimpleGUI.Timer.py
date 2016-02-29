# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "Helper" functions
def increment():
    global counter
    counter = counter + 5

# Define event handlers functions
def tick():
    increment()
    print counter

def buttonpress():
    global counter
    counter = 0
    
# Create a frame
frame = simplegui.create_frame("Test", 100, 100)

# Register event handlers
timer = simplegui.create_timer (2000, tick)
frame.add_button ("Click here!", buttonpress)

#Start frame and timer
frame.start()
timer.start()