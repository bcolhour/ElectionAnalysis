# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
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
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("../analysis", "election_analysis.txt")

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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    # print(headers)
#Print each row in the CSV file. 
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1
        # Print the candidate name for each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
                 # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] =0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save results to text file
with open (file_to_save,"w") as txt_file:
# Print the final vote count to the terminal
    election_results= (
        f"\nElection Results\n"
        f"_________________________\n"
        f"Total Votes: {total_votes:,}\n"
        f"_________________________\n")

    print(election_data, end ="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
        # 2. Retrieve vote count of a candidate
  
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate, their voter count, and percentage to the terminal.
    # 1. Iterate through the candidate list.

        print(candidate_results)
        txt_file.write(candidate_results)

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
       
    winning_candidate_summary = (
        f"__________________________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"___________________________________\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to txt file_reader
    txt_file.write(winning_candidate_summary)
