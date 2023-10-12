# import random
# import time
# import json
# import datetime
# # from mycolors import *
# # from leaderboard import *



# ...
# mypractice_name=''

# Function to read commands from a file
def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Specify the filename for DevOps-related commands
devops_filename = "devops_commands.txt"
devops_commands = read_commands_from_file(devops_filename)


# Specify the filename for hacking-related commands
ethical_hacking_filename = "hacking_commands.txt"
ethical_hacking_commands = read_commands_from_file(ethical_hacking_filename)



# Function to get the basic commands file based on the terminal option
def get_basic_commands_file(terminal_option):
    global mypractice_name
    if terminal_option == 1:
        mypractice_name='basic_commands_termux'
        return "basic_commands_termux.txt", mypractice_name
    elif terminal_option == 2:
        mypractice_name='basic_commands_windows_cmd'
        return "basic_commands_windows_cmd.txt", mypractice_name
    elif terminal_option == 3:
        mypractice_name='basic_commands_windows_powershell'
        return "basic_commands_windows_powershell.txt", mypractice_name
    elif terminal_option == 4:
        mypractice_name='basic_commands_linux_terminal'
        return "basic_commands_linux_terminal.txt", mypractice_name
    else:
        return None


# ...


