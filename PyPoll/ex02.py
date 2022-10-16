import os
import csv
os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyPoll\Resources')
total = 0
list_cand = []
tally = []
per = []
candidates = {}


with open("election_data.csv", "r") as file:
    ed = csv.reader(file, delimiter=",")
    next(ed, None)
    for row in ed:
        if row[2] not in list_cand:
            list_cand.append(row[2])
        total = int(total) + 1
    for name in list_cand:
        tally.append(0)
        #i = int(list_cand.index(name))
        # if row[2] == name:
        #tally[i] = int(tally[i]) + 1
with open("election_data.csv", "r") as file:
    eds = csv.reader(file, delimiter=",")
    next(eds, None)
    for row in eds:
        for name in list_cand:
            i = list_cand.index(name)
            if row[2] == list_cand[i]:
                tally[i] += 1
        # if row[2] == list_cand[0]:
        #     tally[0] = tally[0] + 1
        # elif row[2] == list_cand[1]:
        #     tally[1] = tally[1] + 1
        # else:
        #     tally[2] = tally[2] + 1
for votes in tally:
    ita = tally.index(votes)
    value = tally[ita]/total*100
    value = round(value, 3)
    per.append(value)

print(f"{list_cand}")
print(f"{total}")
print(f"{tally}")
print(f"{per}")
outcome = zip(list_cand, per, tally)
a = 0
max = 0
for n in per:
    if n > max:
        a = per.index(n)
        max = n
winner = list_cand[a]
print(winner)
