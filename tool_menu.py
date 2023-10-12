# import random
# import time
# import json
# import datetime
from mycolors import *
from leaderboard import *

# ...
from startPractice import *


# ...

def display_main_menu():
    print("Welcome to the Command Practice Tool")
    while True:
        print("Choose an option:")
        print("1. DevOps related commands")
        print("2. Ethical Hacking related commands")
        print("3. Basic commands")
        print("4. Leaderboard")
        print("5. Quit")

        choice = input("Enter the option number: ")
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("Invalid choice. Please choose a valid option.")

def display_practice_level_options():
    print("Choose practice level:")
    print("1. 10 commands practice")
    print("2. 30 commands practice")
    print("3. 50 commands practice")
    level_choice = input("Enter the practice level: ")
    if level_choice in ('1', '2', '3'):
        return level_choice
    else:
        print("Invalid practice level. Please choose a valid option.")



# Function to display menu for basic command options
def display_basic_commands_menu(mypractice_name='basic_commands'):
    print("Choose terminal commands options:")
    print("1. Termux")
    print("2. Windows CMD")
    print("3. Windows PowerShell")
    print("4. Linux Terminal")

    terminal_option = int(input("Enter the option number: "))
    if terminal_option in (1, 2, 3, 4):
        practice_basic_commands(terminal_option)
    else:
        print("Invalid terminal option. Please choose a valid option.")


       

