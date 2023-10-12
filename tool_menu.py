# tool_menu.py

# Function to display the main menu and get user choice
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

# Function to display practice level options for DevOps commands
def display_devops_practice_options():
    print("Choose practice level:")
    print("1. 10 commands practice")
    print("2. 30 commands practice")
    print("3. 50 commands practice")
    level_choice = input("Enter the practice level: ")
    if level_choice in ('1', '2', '3'):
        return level_choice
    else:
        print("Invalid practice level. Please choose a valid option.")

