# ElectionAnalysis

## Project Overview
A Colorado Board of Elections employee has requested an election audit of a recent congressional election. 

### Audit Steps
1. Calculate total votes cast. 
2. Compile a complete list of candidates who received votes. 
3. Calculate total number of votes for each candidate. 
4. Calculate percentage of total votes for each candidate. 
5. Determine winner based on popular vote. 

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.6.1, Visual Studio Code, 1.72.2

##Summary
The analysis of the election show that: 
 - There were 369,711 total votes cast in the election. 
 - 3 candidates received votes: 
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
 - Election results by candidate: 
      - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes
      - Diana DeGette received 73.8% of the vote and 272,892 total votes
      - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
  - Election Winner: 
      -Diana DeGette with 272,892 votes equal to 73.8% of the popular vote

## Challenge Overview
The challenge consisted of compiling data form the voter submissions for the congressional election. This consisted of retrieving the following information from a .csv file:
  - Total votes cast
  - How many candidates received votes
  - Total number of votes for each candidate. 
  
Using this information we were able to calculate percentage of votes won and the winner of the popular vote. 

### The process
Variables were assigned to load and open .csv file. 

![image](https://user-images.githubusercontent.com/114044192/196839495-98d5c3bc-eff8-40dc-b308-c541c87a6f91.png)

A total vote counter was set to 0 and the list and dictionary was created to hold our keys and values. The winning Candidate and winning count tracker were set.

![image](https://user-images.githubusercontent.com/114044192/196839933-186bbda2-0ec6-4859-9f09-0d3c4bb58571.png)

The rows were read with both 'for' and 'if' statements used to pull out the information as rach row in the list iterated to determine total votes, number of candidates voted for and votes for each candidate.

![image](https://user-images.githubusercontent.com/114044192/196840326-807bab93-4915-47b8-a61c-99c27ea5b549.png)

A 'for' statement was used to determine percentage of votes using a formula. 

![image](https://user-images.githubusercontent.com/114044192/196840648-cd09e334-29c0-4ab5-a6aa-34119facc667.png)

Finally, the winning candidate was detmined based on anylisis of data. 

![image](https://user-images.githubusercontent.com/114044192/196840944-832fdeb9-fd59-472e-aa58-648adf02b156.png)

## Challenge Summary
I learned a lot in this challenge. The Visual Studio Code makes writing code easier in my opinion. I was able to effectively troubleshoot and correct issues. Several times I found that my issue was incorrect indentation. I feel like I have a fairly good grasp of the concepts and enjoyed this weeks module. It gets confusing repeatedly changing and updating the code as part of the learning process and caused errors to be more likely. However, this accelerated the understanding and learning process and increased my efficiency at identifying issues and successfully correct them. 







  
      
