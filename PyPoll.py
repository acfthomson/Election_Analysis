# Import dependencies: csv and os modules
import csv
import os


# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")


# Open the election results and read the file
with open(file_to_load) as election_data:


    # Read the file object with the reader function
    file_reader = csv.reader(election_data)


    # Skip the first row (headers) in "election_results.csv"
    headers = next(file_reader)


    # Print each row in "election_results.csv"
    for row in file_reader:
        print(row)


# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Use the open() function with "w" mode to write data to the file
with open(file_to_save, "w") as txt_file:


    # Write three counties to "election_analysis.txt". "\n" will put each county on their own line.
    txt_file.write("Counties in the Election")
    txt_file.write("\n________________________")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    

# Close the file
txt_file.close()



# Total number of votes cast
# Row 2 to End Row


# A complete list of candidates who received votes
# How many unique names (candidates)


# Total number of votes each candidate received


# Percentage of votes each candidate won


# The winner of the election based on popular vote


