#!/usr/bin/python3

##
## Reverse inputted text. Run with Python 3.
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

user_string = input("Gimme some characters: ")
user_list = list(user_string)
for i in range(0, len(user_string)):
    print(user_list.pop(), end="")
print()
