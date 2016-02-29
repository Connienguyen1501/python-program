# Stopwatch: The Game

import simplegui

# define global variables
interval = 100
count = 0
total_stops = 0
sucess_stops = 0
stop = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = 0
    B = 0
    C = 0
    D = t

    if t >= 10:
        C = t // 10
        D = t % 10

        if C >= 10:
            B = C // 10
            C = C % 10

            if B >= 6:
                A = B // 6
                B = B % 6

    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    global count, stop
    stop = False
    timer.start()
    
def Stop():
    global total_stops, success_stops, stop
    if stop == False :
        if count % 10 == 0 and count != 0 :
            success_stops += 1
            total_stops += 1
        elif count != 0 :
            total_stops += 1
    stopped = True
    timer.stop()
    
def Reset():
    global count, success_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    success_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1
    

# define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (190,30), 24, "blue")
    
# Create a frame 
frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('black')

# Register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
Reset()
