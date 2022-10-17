import os
import csv
# os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyPoll\Resources')
path = 'Resources/election_data.csv'
total = 0
list_cand = []
tally = []
per = []

with open(path, "r") as file:
    ed = csv.reader(file, delimiter=",")
    next(ed, None)
    for row in ed:
        if row[2] not in list_cand:
            list_cand.append(row[2])
        total = int(total) + 1
    for name in list_cand:
        tally.append(0)
with open(path, "r") as file:
    eds = csv.reader(file, delimiter=",")
    next(eds, None)
    for row in eds:
        for name in list_cand:
            i = list_cand.index(name)
            if row[2] == list_cand[i]:
                tally[i] += 1
for votes in tally:
    ita = tally.index(votes)
    value = tally[ita]/total*100
    value = round(value, 3)
    per.append(value)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

a = 0
max = 0
for n in per:
    if n > max:
        a = per.index(n)
        max = n
winner = list_cand[a]

lines = [("Election Results"), ("-------------------------"),
         (f"Total Votes: {total}"), ("-------------------------")]

for name in list_cand:
    j = list_cand.index(name)
    print(f"{list_cand[j]}: {per[j]}% ({tally[j]})")
    lines.append((f"{list_cand[j]}: {per[j]}% ({tally[j]})"))

lines.append(("-------------------------"))
lines.append((f"Winner: {winner}"))
lines.append(("-------------------------"))

print("-------------------------")
print(f"Winner: {winner}")

# os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyPoll\analysis')
path_a = 'analysis/Analysis.txt'
with open(path_a, 'w') as b:
    for line in lines:
        b.write(line)
        b.write('\n')
