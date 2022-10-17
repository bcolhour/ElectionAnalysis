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
with open(file_to_load) as election_data:
    # Print the file object.
    #print(election_data)
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file. 
    #for row in file_reader:
        #print(row)
    # Print the header row
    headers = next(file_reader)
    print(headers)
    

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

