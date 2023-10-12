# import random
# import time
# import json
# import datetime
# mypractice_name=''

from mycolors import *
from leaderboard import *
from tool_menu import *


if __name__ == "__main__":
    while True:
        choice = display_main_menu()
        

        if choice == '1':
            mypractice_name='devops_commands'
            level_choice = display_practice_level_options()
            if level_choice == '1':
                practice_commands(devops_commands, 10, mypractice_name)
            elif level_choice == '2':
                practice_commands(devops_commands, 30, mypractice_name)
            elif level_choice == '3':
                practice_commands(devops_commands, 50, mypractice_name)

        elif choice == '2':
            mypractice_name='hacking_commands'
            level_choice = display_practice_level_options()
            if level_choice == '1':
                practice_commands(ethical_hacking_commands, 10, mypractice_name)
            elif level_choice == '2':
                practice_commands(ethical_hacking_commands, 30, mypractice_name)
            elif level_choice == '3':
                practice_commands(ethical_hacking_commands, 50, mypractice_name)


        elif choice == '3':
            display_basic_commands_menu()

        elif choice == '4':
            show_leaderboard()

        elif choice == '5':
            print("Goodbye!")
            break


