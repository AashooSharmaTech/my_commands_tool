import random
import time
# import json
# import datetime
from mycolors import *
from leaderboard import *
from fileMenager import *


# ...


def practice_commands(command_list, total_commands, mypractice_name):
    score = 0
    total_time = 0
    random.shuffle(command_list)

    for i in range(total_commands):
        command = command_list[i]
        print(f"Command {i + 1}: {BLUE}{command}{RESET}")  # Blue for the command

        start_time = time.time()
        user_input = input("Enter the command: ")
        end_time = time.time()

        if user_input == command:
            print(f"{GREEN}Correct!{RESET}")  # Green for "Correct!"
            time_taken = end_time - start_time
            total_time += time_taken
            speed = len(command) / time_taken
            score += 1
            print(f"Time taken: {time_taken:.2f} seconds")
            print(f"Typing speed: {speed:.2f} characters per second\n")
        else:
            print(f"{RED}Incorrect!{RESET}\n")  # Red for "Incorrect!"
            score -= 1

    average_time = total_time / total_commands
    print(f"Practice completed. Your score: {YELLOW}{score}/{total_commands}{RESET}")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time per command: {average_time:.2f} seconds")

    user_name = input("Enter your name: ")
    add_score(user_name, score, total_time, mypractice_name)


def practice_basic_commands(terminal_option):
    file_name, mypractice_name = get_basic_commands_file(terminal_option)
    if file_name:
        commands = read_commands_from_file(file_name)
        total_commands = len(commands)  # Adjust total commands based on the chosen file
        practice_commands(commands, total_commands, mypractice_name)
    else:
        print("Invalid terminal option. Please choose a valid option.")




# ...


