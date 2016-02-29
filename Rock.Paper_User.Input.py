def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1      
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "Invaid input"
   
      

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invaid input"  
   
import random
        
# Create an input

import simplegui

def output():
    """prints contents of player choice"""
    print "Player plays", player_choice
    result()
    print ""
    print comp_number
    print player_number
    print result


def enter(inp):
    global player_choice
    player_choice = inp
    output()
    
frame = simplegui.create_frame("rpsls",300,300)
    
frame.add_input("Enter your choice", enter, 200)

#Start frame
frame.start()

# print a blank line to separate consecutive games
print

# convert the player's choice to player_number using the function name_to_number()
def player_choice():
    
    player_number = name_to_number(player_choice)

# compute random guess for comp_number using random.randrange()
comp_number = random.randrange(0, 5)

# convert comp_number to comp_choice using the function number_to_name()
comp_choice = number_to_name(comp_number)
    
# print out the message for computer's choice
print "Computer plays " + comp_choice
    
# compute difference of comp_number and player_number modulo five
def player_number():
    result = (comp_number - player_number) % 5
    
# determine winner, print winner message

def result():
    if result == 1 or result == 2:
       print "Computer wins!"
    elif result == 3 or result == 4:
       print "Player wins!"
    else:
       print "Player and computer tie!"





        

    
    
    