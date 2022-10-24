# Election Analysis

## Project Overview
A Colorado Board of Elections employee has requested an election audit of a recent congressional election. 

### Audit Steps
1. Calculate total votes cast. 
2. Compile a complete list of candidates who received votes. 
3. Calculate total number of votes for each candidate. 
4. Calculate percentage of total votes for each candidate. 
5. Determine winner based on popular vote. 
6. Determine how many votes for each county. 
7. Determine percentage of county votes to total votes cast. 
8. Determine county with highest voter turnout.

### Resources
 - Data Source: election_results.csv
 - Software: Python 3.6.1, Visual Studio Code, 1.72.2

## Election Audit Results
The analysis of the election shows that: 

#### Total Votes Cast
     There were 369,711 total votes cast in the election. 
 
#### Election Results by County- 
    3 counties participated in the vote:
    
        Jefferson County had 10.5% and 38,855 out of total votes
    
        Denver County had 82.8% and 306,055 out of total votes
    
        Arapahoe County had 6.7% and 24,801 out of total votes
    
##### Largest County Turnout: 
 
    Denver had the highest voter turnout by county. 
     
#### Results by Candidate     
##### The Candidates
    3 candidates received votes: 
        Charles Casper Stockham
        Diana DeGette
        Raymon Anthony Doane
    
##### Candidate Statistics: 
      Charles Casper Stockham received 23.0% of the vote and 85,213 total votes
      
      Diana DeGette received 73.8% of the vote and 272,892 total votes
      
      Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
      
##### Election Winner: 
      Diana DeGette with 272,892 votes equal to 73.8% of the popular vote

## Election-Audit Summary
This script could be used to determine the outcome of any election, including pass/fail initiatives. It would also be possile to determine voter turnout for each county based on populaton for the county and votes cast for the county. This would give a better idea of which counties strongly participate in the voting process and the weaker counties that may need additional encouragement to participate. This script can easily accomodate any number of candidates and/or counties. 

## Challenge Overview
The challenge consisted of compiling data form the voter submissions for the congressional election. This consisted of retrieving the following information from a .csv file:
  - Total votes cast
  - How many candidates received votes
  - Total number of votes for each candidate
  - Votes per county
  
Using this information we were able to calculate percentage of votes won, county vote statistics and the winner of the popular vote. 

### The process
Variables were assigned to load and open .csv file. 

![loadVariables](https://user-images.githubusercontent.com/114044192/197444221-c38d9bd9-64fb-415a-a73c-4844ba6bd1f8.PNG)

A total vote counter was set to 0 and the list and dictionary was created to hold our keys and values. The winning Candidate tracker was set, & the winning count tracker, einning percentage and county trackers were set to 0

![trackers](https://user-images.githubusercontent.com/114044192/197444482-cb7253e5-5606-4bd4-a6a2-765e6ee1f8e3.PNG)

The rows were read with both 'for' and 'if' statements used to pull out the information as rach row in the list iterated to determine total votes, number of candidates voted for, votes for each candidate, and votes per county.

![for](https://user-images.githubusercontent.com/114044192/197444672-cc7f6f69-86d9-4ef8-bebc-dc93f5340b4f.PNG)
![image](https://user-images.githubusercontent.com/114044192/197444744-24e800ca-8ae2-40d5-bcb2-a82a4c1614cc.png)

A 'for' statement was used to determine percentage of votes using a formula. 

![image](https://user-images.githubusercontent.com/114044192/196840648-cd09e334-29c0-4ab5-a6aa-34119facc667.png)
![image](https://user-images.githubusercontent.com/114044192/197444941-2f7ccb5b-a634-4e00-b2aa-08802f043b23.png)

Finally, the winning candidate and largest county turnout was determined based on analysis of data. 

![image](https://user-images.githubusercontent.com/114044192/196840944-832fdeb9-fd59-472e-aa58-648adf02b156.png)
![image](https://user-images.githubusercontent.com/114044192/197445126-5513e03b-adfa-46ea-87ef-8910bcdbb906.png)


## Challenge Summary
I learned a lot in this challenge. The Visual Studio Code makes writing code easier in my opinion. I was able to effectively troubleshoot and correct issues. Several times I found that my issue was incorrect indentation. I feel like I have a fairly good grasp of the concepts and enjoyed this weeks module. It gets confusing repeatedly changing and updating the code as part of the learning process and caused errors to be more likely. However, this accelerated the understanding and learning process and increased my efficiency at identifying issues and successfully correct them. 







  
      
