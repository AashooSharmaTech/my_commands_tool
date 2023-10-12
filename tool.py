import random
import time
from leaderboard import add_score, get_leaderboard
from tool_menu import display_main_menu, display_devops_practice_options

# Function to read commands from a file
def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Specify the filename for DevOps-related commands
devops_filename = "devops_commands.txt"
devops_commands = read_commands_from_file(devops_filename)

# Function to get the basic commands file based on the terminal option
def get_basic_commands_file(terminal_option):
    if terminal_option == 1:
        return "basic_commands_termux.txt"
    elif terminal_option == 2:
        return "basic_commands_windows_cmd.txt"
    elif terminal_option == 3:
        return "basic_commands_windows_powershell.txt"
    elif terminal_option == 4:
        return "basic_commands_linux_terminal.txt"
    else:
        return None

def practice_commands(command_list, total_commands):
    score = 0
    total_time = 0
    random.shuffle(command_list)

    for i in range(total_commands):
        command = command_list[i]
        print(f"Command {i + 1}: {command}")
        
        start_time = time.time()
        user_input = input("Enter the command: ")
        end_time = time.time()
        
        if user_input == command:
            print("Correct!")
            time_taken = end_time - start_time
            total_time += time_taken
            speed = len(command) / time_taken
            score += 1
            print(f"Time taken: {time_taken:.2f} seconds")
            print(f"Typing speed: {speed:.2f} characters per second\n")
        else:
            print("Incorrect!\n")
            score -= 1

    average_time = total_time / total_commands
    print(f"Practice completed. Your score: {score}/{total_commands}")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time per command: {average_time:.2f} seconds")
    
    add_score(score)

def practice_basic_commands(terminal_option):
    file_name = get_basic_commands_file(terminal_option)
    if file_name:
        commands = read_commands_from_file(file_name)
        total_commands = len(commands)  # Adjust total commands based on the chosen file
        practice_commands(commands, total_commands)
    else:
        print("Invalid terminal option. Please choose a valid option.")

def practice_ethical_hacking_commands():
    # Add options for Ethical Hacking commands
    ethical_hacking_commands = read_commands_from_file("ethical_hacking_commands.txt")
    total_commands = len(ethical_hacking_commands)
    practice_commands(ethical_hacking_commands, total_commands)

def practice_basic_commands_menu():
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

if __name__ == "__main__":
    while True:
        choice = display_main_menu()

        if choice == '1':
            level_choice = display_devops_practice_options()
            if level_choice == '1':
                practice_commands(devops_commands, 10)
            elif level_choice == '2':
                practice_commands(devops_commands, 30)
            elif level_choice == '3':
                practice_commands(devops_commands, 50)

        elif choice == '2':
            practice_ethical_hacking_commands()

        elif choice == '3':
            practice_basic_commands_menu()

        elif choice == '4':
            show_leaderboard()

        elif choice == '5':
            print("Goodbye!")
            break

