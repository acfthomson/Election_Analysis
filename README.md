# Election_Analysis

## Project Overview
The Colorado Board of Elections requested an audit of a recent local congressional election.  The Colorado Board of Elections requested to find the following:
1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. List the counties that received votes
4. Calculate the total number of votes each candidate received
5. Total number of votes by county
6. Calculate the percentage of votes each candidate won
7. Determine the county with the largest voter turnout
8. Determine the winner of the election based on popular vote

## Resources
 - Data Source: [election_results.csv](https://github.com/acfthomson/Election_Analysis/blob/main/election_results.csv)
 - Software: Python v3.7.6 and Visual Studio Code v1.51.1
  
## Summary
The Python code needed to use for loops and conditional statements with membership and logical operators to find the requested results. It then needed to print the results to the command line and save them to [election_analysis.txt](https://github.com/acfthomson/Election_Analysis/blob/main/election_analysis.txt).

This Python script required two dependencies: csv and os. These packages allow Python to read CSVs and interact with the operating system.
```python
# Add our dependencies
import csv
import os

# Add a variable to load a file from a path
file_to_load = os.path.join(".", "Resources", "election_results.csv")
# Add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

This code snippet will initialize variables, lists, and dictionaries for candidates and counties.

```python
total_votes = 0

candidate_options = []
candidate_votes = {}

county = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0
```

Python will then track the largest county and county voter turnout.  It will read a CSV, convert it into a list of dictionaries, and tally the total vote and get candidate names using a for-loop.

```python
largest_turnout = ""
winning_turnout = 0

with open(file_to_load) as election_data:    
        reader = csv.reader(election_data)    
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
```
 
Here, the county name's are extracted from each row of the CSV.  An if-statement is used to find unique candidate names, add them to the list, and then begin tracking the candidate's vote count. 
```python 
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0            
        candidate_votes[candidate_name] += 1        
```

Another if-statement is used that checks if the county is already in the list.  If it is not, it is added to the list and then begins tracking the county's vote count.
```python
        if county_name not in county:        
            county.append(county_name)
            county_votes[county_name] = 0           
```            

This code snippet will add a vote to that county's vote count.
```python
county_votes[county_name] += 1
```

Python will save the results of the counts to election_analysis.txt and also print them to the terminal.
```python
with open(file_to_save, "w") as txt_file: 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")   
    txt_file.write(election_results)
```    

A for-loop is used to get the county from the county dictionary, calculate percentage of votes for the county, print them to the terminal, and also write the county votes to election_analysis.txt.  An if-statement is used to determine the winning county and get its vote count.
```python
    for county_name in county:
        turnout = county_votes[county_name]
        turnout_percentage = float(turnout) / float(total_votes) * 100
        county_results = (f'{county_name}: {turnout_percentage:.1f}% ({turnout:,})\n')
        print(county_results)
        txt_file.write(county_results)
        if (turnout > winning_turnout):
            winning_turnout = turnout
            largest_turnout = county_name
```

f-strings are used to print out the county with the largest turnout to the terminal.
```python
    largest_turnout_summary = (
        f"--------------------------\n"
        f"Largest Turnout: {largest_turnout}\n"
        f"--------------------------\n"
    )
    print(largest_turnout_summary)

This part of the code saves the county with the largest voter turnout, final candidate vote count, and percentage to election_analysis.txt.  These values are also printed to the terminal.  
```python
    txt_file.write(largest_turnout_summary)

    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
```

### Election Results
    - Total Votes: 369,711

    - County Votes:
        - Jefferson: 10.5% (38,855)
        - Denver: 82.8% (306,055)
        - Arapahoe: 6.7% (24,801)

    - Largest Turnout: Denver

    - Vote Total By Candidate:
        - Charles Casper Stockham: 23.0% (85,213)
        - Diana DeGette: 73.8% (272,892)
        - Raymon Anthony Doane: 3.1% (11,606)

    - Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%


### Election Audit Summary
It is recommended that the Colorado Board of Elections maintain this script for future use so that it can be refactored for future elections, which could have different candidates or different counties.
