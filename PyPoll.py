# Import dependencies: csv and os modules
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
# This must be placed before the "with open()" statement
# This variable must be set to zero everytime the file is executed
total_votes = 0

# List of candidates
candidate_options = []

# Dictionary to link votes to candidates 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
# This variable will hold an empty string value for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Skip the first row (headers) in "election_results.csv" and go to the next item
    headers = next(file_reader)

    # Print each row in "election_results.csv"
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Only print unique candidate names
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Track candidate's vote count, but first set to zero
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to the text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    # election_results will have four variables written to it
    election_results = (
        f"\nElection Results\n"
        f"\n------------------------------------\n"
        # total_votes will print with votes formatted with a thousands separator
        f"\nTotal Votes: {total_votes:,}\n"
        f"\n------------------------------------\n")
    # election_results will with the parameter end="", which is equal to an empty string
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

    # Print candidate vote dictionary
    print(candidate_votes)

    # Calculate percentage of votes for each candidate by looping through counts
    # Votes are values of each candidate_name in candidate_votes dictionary
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        # Convert votes and total_votes to floats because both are integers
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: Print out each candidate's name, vote count, and percentage of votes
        # Add each candidate's election results to election_analysis.txt
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true, then set winning_count = votes
            # and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)