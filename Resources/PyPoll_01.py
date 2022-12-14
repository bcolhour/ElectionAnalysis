# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidats who received votes
# 3. The percentagge of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
# Assign a variable for the file to load and the path.
    #file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
        #election_data = open(file_to_load,'r')
    #with open(file_to_load) as election_data:         
# To do: perform analysis.
#    print(election_data)
# Close the file.
    #election_data.close()
#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.

# 1. Initialize a total vote counter. 
total_votes=0

# Declare new list
candidate_options = []
# Declare empty dictionary
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file. 
    #for row in file_reader:
        #print(row)
    # Print the header row
    headers = next(file_reader)
    print(headers)
#Print each row in the CSV file. 
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1
        # Print the candidate name for each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
                 # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking htat candidates vote count
            candidate_votes[candidate_name] =0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes)*100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
    # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    winning_candidate_summary = (
        f"__________________________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"___________________________________\n"
    )
print(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

# 3. Print the total votes
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)

# 4. Print the candidate name and percentage of votes
#print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote. ")


# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


# Use the open statement to open the file as a text file.
    #outfile = open(file_to_save,"w")
# Write some data to the file.
    #outfile.write("Hello World")
# close the file
#outfile.close()

# Cleaner method - Using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n____________________________________\nArapahoe\nDenver\nJefferson")

