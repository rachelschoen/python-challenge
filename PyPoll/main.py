# Importing necessary modules.

import csv
from operator import itemgetter

# Open CSV file and read data into a list of dictionaries.

with open('./Resources/election_data.csv', 'r') as myFile:
    reader = csv.DictReader(myFile)
    electionData = list(reader)

# Print header
print("Election Results")
print("-------------------------")

# Print the total number of votes cast.
numVotes = len(electionData)
print(f"Total Votes: {numVotes}")
print("-------------------------")

# Sort the nested list by candidate.
sortedElectionData = sorted(electionData, key=itemgetter('Candidate'))

# Next, we'll calculate each required calculation step-by-step.

# 1) Count the number of votes, calculate the percentage of election won, and then add to the message list.


#     a) Prepare the variables for the iteration of all votes.
name = sortedElectionData[0]['Candidate']
numCandidates = 0
voteCount = 0
winnerName = ""
winnerPercentage = 0
message = []

#     b) Enter for-loop, knowing the list of votes is sorted by candidate.)
for i in range(0, numVotes):
    row = sortedElectionData[i]

    # If the name matches the candidate, add to the voteCount.
    if row['Candidate'] == name:
        voteCount += 1
    else:
        # Calculate percentage of votes out of total.
        percentage = round(voteCount/numVotes*100, 3)
        
        # Check if it beats the largest percentage we have stored.
        if percentage > winnerPercentage:
            winnerName = name
            winnerPercentage = percentage
        
        # Add our previous candidate's name, votes, and percentage to the message list.
        print(f"{name}: {percentage}% ({voteCount})")
        message.append(name + ": " + str(percentage) + "% " + "(" + str(voteCount) + ")")
        
        # Update the variables for our current candidate.
        numCandidates += 1
        name = row['Candidate']
        voteCount = 1 # This is because we did not add a vote to the count yet.


# 2) We've finished the for-loop, but we still need to print the last candidate's name, votes, and percentage.
        
#     a) Calculate percentage of votes out of total
percentage = round(voteCount/numVotes*100, 3)

#     b) Check if it's the winner
if percentage > winnerPercentage:
    winnerName = name
    winnerPercentage = percentage

#     c) Add our last candidate's name, votes, and percentage to the message list
message.append(name + ": " + str(percentage) + "% " + "(" + str(voteCount) + ")")

#     d) Print out the winner name, percentage won by, and total votes received
print(f"{name}: {percentage:.3f}% ({voteCount})")
print("-------------------------")
print(f"Winner: {winnerName}")
print("-------------------------")

# Finally, we'll print the message list to output.txt.

with open("output.txt", "w") as textFile:
    textFile.write("Election Results\n")
    textFile.write("-------------------------\n")
    textFile.write(f"Total Votes: {numVotes}\n")
    textFile.write("-------------------------\n")
    for line in message:
        textFile.write(f"{line}\n")
    textFile.write("-------------------------\n")
    textFile.write(f"Winner: {winnerName}\n")
    textFile.write("-------------------------\n")