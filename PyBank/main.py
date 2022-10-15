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
        if change_occurred > inc:
            inc = change_occurred
            inc_month = row[0]
        if change_occurred < dcr:
            dcr = change_occurred
            dcr_month = row[0]
        previous_value = row[1]

change.pop(0)


def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total/length


avg = average(change)
avg = round(avg, 2)
# print(f"{count}")
# print(f"{net}")
# print(f"{change}")
#check = len(change)
# print(f"{check}")
print(f"Total months: {count}")
print(f"Total: ${net}")
print(f"Average change: ${avg}")
print(f"Greatest increase in profits: {inc_month} (${inc})")
print(f"Greatest decrease in profits: {dcr_month} (${dcr})")
