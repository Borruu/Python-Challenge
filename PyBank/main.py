from calendar import month
import os
import csv
os.getcwd()
os.chdir(r'C:\Users\30798\Desktop\Python\Module_03_Python2\Python-Challenge\PyBank\Resources')
# c:/Users/30798/Desktop/Python/Module_03_Python2/Python-Challenge/PyBank/Resources')
count = 0
net = 0
current_value = 0
previous_value = 0
change_occurred = 0
change = []
avg = 0.00
inc = 0
inc_month = "month"
dcr = 0
dcr_month = "month"


with open("budget_data.csv", "r", encoding="utf") as budget:
    rb = csv.reader(budget, delimiter=",")
    header = next(budget)

    for row in rb:
        count = count + 1
        current_value = int(row[1])
        net = (net + current_value)
        change_occurred = (current_value - int(previous_value))
        change.append(change_occurred)
        previous_value = row[1]
print(f"{count}")
print(f"{net}")
print(f"{change}")
check = len(change)
print(f"{check}")
