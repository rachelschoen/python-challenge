# Importing necessary modules.

import csv
from datetime import datetime as dt
from operator import itemgetter

# Open CSV file and read data into a list of dictionaries.

with open('./Resources/budget_data.csv', 'r') as myFile:
    reader = csv.DictReader(myFile)
    budgetData = list()
    for dictionary in reader:
        budgetData.append(dictionary)

# Add a sortable date to each dictionary.
for row in budgetData:
    date =  row['Date']
    new_date = dt.strptime(date, '%b-%y').strftime('%y/%m')
    row['sortableDate'] = new_date

# Sort by the sortable date key.
sortedBudgetData = sorted(budgetData, key=itemgetter('sortableDate'))

# Print our message header to the terminal.
print("Financial Analysis")
print("----------------------------")

# Find and print the total number of months included in the dataset.
prevDate = ""
numMonths = 0
for row in sortedBudgetData:
    date = row['Date']
    if date != prevDate:
        numMonths += 1
print(f"Total Months: {numMonths}")

# Find, then total, then print, the net amount of "Profit/Losses" over the entire period.
net = 0
for row in budgetData:
    net += int(row['Profit/Losses'])
print(f"Total: ${net}")

# Calculate and print the average change in "Profit/Losses" between months, over the entire period.

sumChanges = 0
previousValue = int(budgetData[0]['Profit/Losses'])
for row in budgetData:
    row['Change'] = int(row['Profit/Losses']) - previousValue
    sumChanges += row['Change']
    previousValue = int(row['Profit/Losses'])
avgChange = sumChanges/(len(budgetData) -1)
print("Average Change: ${:.2f}".format(avgChange))

# Find and print the greatest increase and decrease in profits (both the date and the amount), over the entire period.
maxIncrValue = 0
maxIncrDate = ""
maxDecrValue = 0
maxDecrDate = ""
for row in budgetData:
    if int(row['Change']) > maxIncrValue:
        maxIncrValue = int(row['Change'])
        maxIncrDate = row['Date']
    if int(row['Change']) < maxDecrValue:
        maxDecrValue = int(row['Change'])
        maxDecrDate = row['Date']

print(f"Greatest Increase in Profits: {maxIncrDate} (${maxIncrValue})")
print(f"Greatest Decrease in Profits: {maxDecrDate} (${maxDecrValue})")