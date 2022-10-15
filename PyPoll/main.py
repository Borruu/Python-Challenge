import os
import csv
os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyPoll\Resources')
with open("election_data.csv", "r") as file:
    ed = csv.reader(file, delimiter=",")
    next(ed, None)
