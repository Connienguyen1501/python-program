# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = 0.0
paddle2_pos = 0.0
paddle1_vel = 0.0
paddle2_vel = 0.0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    horizon_vel = random.randrange(120, 240)/50.0
    if direction == "LEFT":
        horizon_vel = -horizon_vel
    vertical_vel = -random.randrange(60, 180)/50.0
    ball_vel = [horizon_vel, vertical_vel] 


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    score1 == 0
    score2 == 0
    # new game ball will go randomly right or left
    spawn_ball(random.choice(["LEFT","RIGHT"]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
     # call spawn_ball and increment score if ball hits a gutter
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] - paddle1_pos) > (HEIGHT - 3 * PAD_HEIGHT) and (ball_pos[1] - paddle1_pos) < (HEIGHT - 2 * PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            
            # ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score2 = score2 + 1
            spawn_ball("RIGHT")
    if ball_pos[0] >= ((WIDTH - 1) - PAD_WIDTH - BALL_RADIUS):
        if (ball_pos[1] - paddle2_pos) > (HEIGHT - 3 * PAD_HEIGHT) and (ball_pos[1] - paddle2_pos) < (HEIGHT - 2 * PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            # ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score1 = score1 + 1
            spawn_ball("LEFT")
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3, "Blue", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) >= -(HEIGHT/2.0 - HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel) <= (HEIGHT/2.0 - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel) >= -(HEIGHT/2.0 - HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel) <= (HEIGHT/2.0 - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle1_pos), 
                    (PAD_WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle1_pos), 
                    (PAD_WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle1_pos), 
                    (0, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle1_pos)], 1, 'White', 
                    'White')
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH - PAD_WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle2_pos)], 
                    1, 'White', 'White')  
    
   
    # draw scores
    canvas.draw_text(str(score1), (220, 100), 45, 'White', "sans-serif")
    canvas.draw_text(str(score2), (350, 100), 45, 'White', "sans-serif")    

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5

# if control keys are up stop paddles
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame, register draw handler, key handlers, and restart button
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button_reset = frame.add_button('Restart', new_game, 100)

# start frame and start a game immediately
new_game()
frame.start()