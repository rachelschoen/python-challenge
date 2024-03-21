# Importing necessary modules.

import csv
from operator import itemgetter

# Open CSV file and read data into a list of dictionaries.

with open('./Resources/election_data.csv', 'r') as myFile:
    reader = csv.DictReader(myFile)
    electionData = list(reader)

