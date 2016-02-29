import simplegui
import random
import math

# initialize global variables used in the code
secrect_number = 0
remaining_guesses = 7
low = 0
high = 100

# helper functions to initial game
def init():
    range100()
    
# helper function to create a new game
def new_game(low1, high1):
    global secret_number, remaining_guesses, low, high
    low = low1
    high = high1
    secret_number = random.randrange(low, high)
    remaining_guesses = 7
                                  
    print ""
    print "New game. Range is from", low, "to", high
    print "Number of remaining guesses is", remaining_guesses
    
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0, 100] and restarts
    new_game(0,100)

def range1000():
    # button that changes range to range [0, 1000] and restarts
    new_game(0,1000)                        
    
def get_input(guess):
    global secret_number, remaining_guesses
    remaining_guesses = remaining_guesses - 1
    guess = int(guess)
    
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is", remaining_guesses
    
    if remaining_guesses > 0:
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
        else:
            print "Correct!"
            new_game(low,high)
    else:
        if guess == secret_number:
            print "Correct!"
        else:
            print "You ran out of guesses. The number was", secret_number
        new_game(low,high)
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
init()



