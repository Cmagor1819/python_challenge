# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

from param import output

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
# Date = str(file_to_load[0])
# profit_loss = int(file_to_load[1])
# previous_profit_loss = None

# Open and read the csv
with open(file_to_load, newline="") as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(financial_data)
    print(first_row)

    # Track the total and net change
    total_net = []
    Date = []

    # Process each row of data
    for rows in reader:
        total_net.append(int(rows[1]))
        Date.append(rows[0])
        # Track the total
        total_net =[]

        # Track the net change
        net_change = []

    for r in range(1,len(total_net)):
        net_change.append((int(total_net[r]) - int(total_net[r-1])))

        # calculate the total months
        total_months = len(Date)

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(net_change)

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change)

        # Calculate the average net change across the months
        net_average = sum(net_change)/ len(net_change)

    # Print the output
    print("Financial Analysis")

    print("----------------------------")

    print("Total Months: " + str(total_months))

    print("Total: " + "$ " + str(sum(total_net)))

    print("Average Change: " + "$ " + str(net_average))

    print("Greatest Increase in Profit: " + str(total_months[net_change.index(max(net_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profit: " + str(total_months[net_change.index(min(net_change))+1]) + " " + "$" + str(greatest_decrease))

# Write the results to a text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)


