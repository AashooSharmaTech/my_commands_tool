import json
import datetime

leaderboard = []

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
def add_score(user_name, score, total_time):
    achievement_time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")
    leaderboard.append({"user_name": user_name, "score": score, "total_time": total_time, "time": achievement_time})
    save_leaderboard()

# Retrieve the leaderboard in the specified order
def get_leaderboard(sort_by_score=True):
    if sort_by_score:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: (-x["score"], x["total_time"]))
    else:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: (x["total_time"], -x["score"]))
    return sorted_leaderboard

# Initialize leaderboard by loading data
load_leaderboard()

