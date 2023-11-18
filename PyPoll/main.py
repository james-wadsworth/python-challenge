# import os to use for file path
import os

# Import the csv reading module
import csv

# Create variable to hold the csv path
csvfile = os.path.join("Resources", "election_data.csv")
print(csvfile)

# With the csv open, start doing things
with open(csvfile) as csvfile:

    # First bring in the whole file as an iterable object
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Print out the column headers to get bearings
    csv_header = next(csvreader)
    print(csv_header)

    # Calculate the total votes

    # Initiatlize an empty list of votes
    votes = []
    candidates = []

    # Loop through rows and count the first item in each row
    for row in csvreader:

        # Add the item to the empty vote list
        votes.append(row[0])
        candidates.append(row[2])

    # Count total votes by using length of votes list
    total_votes = len(votes)
    unique_cand = list(set(candidates))
    print(total_votes)
    print((unique_cand))

    # Find total votes for each candidate.

    candidate1 = unique_cand[0]
    candidate2 = unique_cand[1]
    candidate3 = unique_cand[2]

    candidate1_votes = []
    candidate2_votes = []
    candidate3_votes = []

    for vote in candidates:
        if vote == candidate1:
            candidate1_votes.append(vote)
        elif vote == candidate2:
            candidate2_votes.append(vote)
        elif vote == candidate3:
            candidate3_votes.append(vote)

    
    print(len(candidate1_votes))
    print(len(candidate2_votes))
    print(len(candidate3_votes))

    # Percentage of the vote
    

