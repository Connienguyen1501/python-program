import simplegui


#####################
# Buggy code -- doesn't start frame

message = "Welcome!"


def click():
    """Change message on mouse click."""
    global message
    message = "Good job!"


def draw(canvas):
    """Draw message."""
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers

frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

#Start frame
frame.start()


