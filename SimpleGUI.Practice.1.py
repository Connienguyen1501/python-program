# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print "This is Connie"
def greeting():
    print "Hello!"
        

# Register handler
timer1 = simplegui.create_timer(3000, tick)
timer2 = simplegui.create_timer(2000, greeting)

# Start timer
timer1.start()
timer2.start()

