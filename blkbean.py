#!/usr/bin/python3

##
## Black bean game. Give launching permissions and execute or execute
## with Python3.
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

import random
import time

print("Whoever takes the last bean wins")
total_beans = int(input("How many total beans: "))
max_beans = int(input("Max beans per turn: "))
#turn_s = input("Would you like to go first? (Y/N): ")
#if (turn_s == "Y" or turn_s == "y"):
#    turn = 1
#else:
#    turn = 0
if total_beans % (max_beans+1) == 0:
    turn = 1
else:
    turn = 0

num_beans = total_beans

while (num_beans > 0):
    take = 0
    print(num_beans, " beans left.")
    if (turn == 0):
        print("My turn!")
        if (num_beans % (max_beans+1) > 0):
            take = num_beans % (max_beans+1)
        else:
            take = random.randint(1,max_beans)
        time.sleep(1)
        print("I take ", take, " beans.")
    elif (turn == 1):
        print("Your turn!")
        while (not(take >= 1 and take <= max_beans)):
            take = int(input("Take how many beans: "))
        print("You take ", take, " beans.")
    num_beans -= take
    if (turn ==0):
        turn = 1
    elif (turn == 1):
        turn = 0
if (turn == 0):
    print("I lose! :(")
elif (turn == 1):
    print("You lose! :)")
