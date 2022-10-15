import os
import csv
os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyPoll\Resources')
total = 0
list_cand = []
tally = []

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
    for row in ed:
        for name in list_cand:
            if row[2] == list_cand(name):
                i = list_cand.index(name)
                tally[i] = int(tally[i]) + 1


print(f"{list_cand}")
print(f"{total}")
print(f"{tally}")

candidates = {}
candidates["Name"] = list_cand

# candidates["Tally"] =
