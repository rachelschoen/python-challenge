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

print(sortedBudgetData)

# Print our message header to the terminal.
print("Financial Analysis")
print("----------------------------")