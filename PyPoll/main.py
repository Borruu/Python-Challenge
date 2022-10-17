import os
import csv

# Navigate to source csv file
path = 'Resources/election_data.csv'

# Variables
total = 0
list_cand = []
tally = []
per = []

# Read csv file
with open(path, "r") as file:
    ed = csv.reader(file, delimiter=",")
    # store header row
    header = next(ed, None)

    # loop through rows to get list of candidates and total number of votes
    for row in ed:
        if row[2] not in list_cand:
            list_cand.append(row[2])
        total = int(total) + 1
    for name in list_cand:
        tally.append(0)

# Loop through rows again to add vote count for each candidate to tally list
with open(path, "r") as file:
    eds = csv.reader(file, delimiter=",")
    next(eds, None)
    for row in eds:
        for name in list_cand:
            i = list_cand.index(name)
            if row[2] == list_cand[i]:
                tally[i] += 1

# Loop through tally list to work out percentage of votes for each candidate, round value to 3 decimal places and store results in per list
for votes in tally:
    ita = tally.index(votes)
    value = tally[ita]/total*100
    value = round(value, 3)
    per.append(value)

# Print results to Terminal for total votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

# Find maximum value in per list to declare winner
a = 0
max = 0
for n in per:
    if n > max:
        a = per.index(n)
        max = n
winner = list_cand[a]

# Store results text to lines list for total votes
lines = [("Election Results"), ("-------------------------"),
         (f"Total Votes: {total}"), ("-------------------------")]

# Concatenate results for each candidate, print to Terminal and add to lines list
for name in list_cand:
    j = list_cand.index(name)
    print(f"{list_cand[j]}: {per[j]}% ({tally[j]})")
    lines.append((f"{list_cand[j]}: {per[j]}% ({tally[j]})"))

# Add winner to lines list
lines.append(("-------------------------"))
lines.append((f"Winner: {winner}"))
lines.append(("-------------------------"))

# Print winner to Terminal
print("-------------------------")
print(f"Winner: {winner}")

# Navigate to analysis folder, create/overwrite Analysis text file with results
path_a = 'analysis/Analysis.txt'
with open(path_a, 'w') as b:
    for line in lines:
        b.write(line)
        b.write('\n')
