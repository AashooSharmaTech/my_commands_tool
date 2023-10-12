
import json
import datetime
from mycolors import *




# Load leaderboard data from JSON file
def load_leaderboard():
    global leaderboard
    try:
        with open("leaderboard.json", "r") as json_file:
            leaderboard = json.load(json_file)
    except FileNotFoundError:
        leaderboard = []

# Save leaderboard data to JSON file
def save_leaderboard():
    with open("leaderboard.json", "w") as json_file:
        json.dump(leaderboard, json_file, indent=4)

# Add a user's score, total time, and achievement time to the leaderboard
def add_score(user_name, score, total_time, pratice_Name):
    achievement_time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")
    leaderboard.append({"user_name": user_name, "score": score, "total_time": total_time, "time": achievement_time, "practice_name":pratice_Name})
    save_leaderboard()

# Retrieve the leaderboard in the specified order
def get_leaderboard(sort_by_score=True):
    if sort_by_score:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: (-x["score"], x["total_time"]))
    else:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: (x["total_time"], -x["score"]))
    return sorted_leaderboard

leaderboard = []

# Initialize leaderboard by loading data
load_leaderboard()


# Function to display the leaderboard
def show_leaderboard():
    leaderboard = get_leaderboard()
    line=120
    print("\nLeaderboard:")
    print("="*line)
    print(f"{'User Name':<20}  {'Score':<10}{'Time Taken (s)':<20}\t{'Achievement Date/Time':<25}\t{'Practice Name':<20}")
    print("="*line)

    for entry in leaderboard:
        user_name = entry['user_name']
        score = entry['score']
        total_time = entry['total_time']
        achievement_time = entry['time']
        # practice_name = entry.get('practice_name', "N/A")  # Retrieve practice name or use "N/A" if not specified
        practice_name = entry['practice_name']

        formatted_time = "{:.2f}".format(total_time)


        # Apply colors to specific fields
        formatted_user_name = f"{CYAN}{user_name}{RESET}"     # Cyan for the username
        formatted_score = f"{YELLOW}{score}{RESET}"           # Yellow for the score
        formatted_total_time = f"{GREEN}{formatted_time}{RESET}"  # Green for total time
        formatted_achievement_time = f"{MAGENTA}{achievement_time}{RESET}"  # Magenta for achievement time
        formatted_practice_name= f"{RED}{practice_name}{RESET}"     # Cyan for the username


        print(f"{formatted_user_name:<20}\t\t{formatted_score:<10}  \t{formatted_total_time:<20}\t\t{formatted_achievement_time:<25}\t\t{formatted_practice_name:<20}")

    print("="*line)

# ...


