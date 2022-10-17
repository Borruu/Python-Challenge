from calendar import month
import os
import csv

# Navigate to source csv file
file = 'Resources/budget_data.csv'

# Variables
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

# Read csv file
with open(file, "r", encoding="utf") as budget:
    rb = csv.reader(budget, delimiter=",")
    # Store header row
    header = next(budget)

# Loop through rows to count months, get total profit/loss, greatest increase, greatest decrease and create list of change values
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
# Remove first value from change list
change.pop(0)

# Function to find average change


def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total/length


# Get average change and round to 2 decimal places
avg = average(change)
avg = round(avg, 2)

# Print results to Terminal
print(f"Total months: {count}")
print(f"Total: ${net}")
print(f"Average change: ${avg}")
print(f"Greatest increase in profits: {inc_month} (${inc})")
print(f"Greatest decrease in profits: {dcr_month} (${dcr})")

# Store results text in list
lines = [(f"Total months: {count}"), (f"Total: ${net}"), (f"Average change: ${avg}"), (f"Greatest increase in profits: {inc_month} (${inc})"),
         (f"Greatest decrease in profits: {dcr_month} (${dcr})")]

# Navigate to analysis folder and create/overwrite Analysis text file with results list
file_a = 'analysis/Analysis.txt'
with open(file_a, 'w') as a:
    for line in lines:
        a.write(line)
        a.write('\n')
