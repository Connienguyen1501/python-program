# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Create "Your name" Text box

def your_name():
    print "Your full name"

# Create "Emai" Text box

def your_email():
    print "Your email address"
    
# Create "Sign In" Text box

def sign_in():
    print "Sign In"
        

# Register handler
frame1 = simplegui.create_frame("Your full name", 100, 50)
frame2 = simplegui.create_frame("Your email address", 100, 50)
frame3 = simplegui.create_frame("Sign In", 50, 25)
frame1.set_canvas_background('Orane')
frame2.set_canvas_background('Orange')
frame3.set_canvas_background('Blue')
print frame1.get_canvas_textwidth("Your full name", 12)
print frame2.get_canvas_textwidth("Your email address", 12)
print frame3.get_canvas_textwidth("Sign In", 12)
frame1.start()
frame2.start()
frame3.start()


