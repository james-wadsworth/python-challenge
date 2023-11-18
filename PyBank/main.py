# Import module to allow creation of file path across operating systems
import os

# Import module for reading CSV files
import csv

# Store the file path to the data file for PyBank
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the file to read it and process the data with python
with open(csvpath, newline='') as csvfile:

    # Create variable to hold the reader object 
    # (this is something that allows us to iterate over lines in the given csv file. 
    # Could be a list as well as a file, but this happens to be a file)
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and show me the header row so I can get my bearings when it comes to this data file
    csv_header = next(csvreader)

    # Show me the contents of the data file head or in other words, list the column names out for me

    # Create an empty list to hold the months
    months = []

    # Create empty list to hold the Profit/Losses column data
    net_profit = []

    # Iterate through the rows
    for row in csvreader:

        # Add Date items to the months list
        months.append(row[0])

        # Add Profit/Losses data items to the net_profit list
        net_profit.append(int(row[1]))

    # Calculate the total number of months in the dataset by finding the number of items in the month list and printing it
    total_months = len(months)
    

    # Calculate the total net profit by adding up the data for each month and then print it.
    total_np = sum(net_profit)
    

    # Find the average month over month change in net profit
    
    # Loop through the list and calculate the change at each interval
    # Create an empty list to hold the changes
    change = []

    # Loop through the net_profit list starting at the second item (skip the header)
    for i in range(1,len(net_profit)):
    
        # Add each calculated change into the empty change list as an integer
        change.append(int(net_profit[i] - net_profit[i - 1]))

    # Calculate the average change and store it in a variable
    average_change = sum(change) / len(change)

    # Find the max month-over-month change
    max = max(change)

    # Find the min
    min = min(change)

    # Find the index of the min and add 1 to get the index of the correct date
    index_spot_min = change.index(min) + 1
    index_spot_max = change.index(max) + 1

    # Print everything cleanly to summarize

    print(
        f'Financial Analysis\n'
          
        f'--------------------------------------- \n\n'

        f'Total Months : {total_months} \n\n'
          
        f'Total: {total_np} \n\n'
          
        f'Average Change: {average_change} \n\n'
          
        f'Greatest Increase in Profits: {months[index_spot_max]} ${max} \n\n'

        f'Greatest Decrease in Profits: {months[index_spot_min]} ${min} \n\n'
          
          )
