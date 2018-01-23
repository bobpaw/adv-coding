##
## The bean game. Run in python 3.
## Author: Jason Kolbly <jason@rscheme.org>
##

print ("Beans are cool!!!")

# Computer's turn
def computer_turn():
    global number_beans
    print ("I'm taking " + str(number_beans % (number_pickable + 1)) + " beans")
    number_beans -= number_beans % (number_pickable + 1)
    print ("Beans left: " + str(number_beans))
    if number_beans < 0:
        print ("You win! You should never get this message.")
        return False
    player_turn()

# Player's turn
def player_turn():
    global number_beans
    take = 0
    while (not(take >= 1 and take <= number_pickable)):
        take = int(input("How many do you want to take? It has to be from 1 to " + str(number_pickable) + " "))
    number_beans -= take
    print ("Beans left: " + str(number_beans))
    if number_beans < 0:
        print ("You lose. Sucks to suck.")
        return False
    computer_turn()

# Assign number_beans and number_pickable
number_beans = 0
number_pickable = 0
while (not(number_beans > 1)):
    number_beans = int(input("How many beans do we want? (Input a number more than 1) "))
while (not(number_pickable < number_beans and number_pickable > 0)):
    number_pickable = int(input("How many can we pick? (Input a number less than the first one) "))

# Test if number_beans and number_pickable are right values, then start
if number_beans > 0 and number_pickable > 0 and number_beans > number_pickable:
    print ("Okay, we have " + str(number_beans) + " beans, and we can pick up to " + str(number_pickable) + " beans on our turn.")
else:
    print ("You can't pick more than there are!")

# Decide who goes first
if number_beans % (number_pickable + 1) == 0:
    print ("You can go first")
    player_turn()
    start = True
else:
    print ("I'll go first")
    computer_turn()
    start = True
