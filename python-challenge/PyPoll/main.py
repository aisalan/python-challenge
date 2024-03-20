#dependencies
import os
import csv

#define file path
election_data_csv = "election_data.csv"
output_file = "election_results.txt"
PyPollcsv = os.path.join(".", "election_data.csv")

#variables
data = []
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

#load the data from the csv file
with open(PyPollcsv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#iteration
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

#%calculation
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

#finding the winner
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# to print results in terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a text file
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

# Print confirmation message
print(f"Election results have been exported to '{output_file}'.")
