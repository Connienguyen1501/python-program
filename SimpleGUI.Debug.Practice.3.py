#####################
# Buggy code -- doesn't start timers

import simplegui

def timer1_handler():
    print "1"
    
def timer2_handler():
    print "2"

timer1 = simplegui.create_timer(100, timer1_handler)
timer2 = simplegui.create_timer(300, timer2_handler)

timer1.start()
timer2.start()