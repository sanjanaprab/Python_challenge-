# Import files needed 
import os
import csv

# Read file 
csvpath = os.path.join('Resources', 'election_data.csv')

# Initializing the variables 
total_votes = 0
candidate_votes = {}

# file reader 
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] +=1

# Calculations 
results = []
winner = {"name": "", "votes": 0}
for candidate, vote in candidate_votes.items():
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}%({votes})")
    if votes > winner["votes"]:
        winner = {"name": candidate, "votes": votes}

# Test Print
print("Hello World")

# Calculations 
print("PyPoll Election Results")
print("_______")
print(f"Total Votes: {total_votes}")
print("_______")
for result in results: 
    print(result)
print("_______")
print(f"Winner: {winner['name']}")
print("_______")

# creating and exporting analysis file for PyPoll
analysis_path = 'election_results.txt'
with open(analysis_path, mode='w') as file:
    file.write("PyPoll Election Results\n")
    file.write("_______\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("_______\n")
    for result in results: 
        file.write(result + "\n")
    file.write("_______\n")
    file.write(f"Winner: {winner['name']}/n")
    file.write("_______\n")


