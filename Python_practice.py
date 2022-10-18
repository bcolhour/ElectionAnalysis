counties = ["Arapahoe","Denver","Jefferson"]
counties_dict={}
counties_dict
{'Arapahoe': 422829, 'Jefferson': 42438, 'Denver': 463353}
voting_data={}
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
    
for county in counties:
    print(county)
for county in counties_dict:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for key, value in counties_dict.items():
    print(key,value)
for county, voters in counties_dict.items():
    print(county, "county has ",voters, "registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):

      print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:

     print(county_dict['county'])
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes= int(input("What is the total votes in the election? "))
#percentage_votes= (my_votes/total_votes)*100
#print("I received " +str(percentage_votes)+"%o of the total votes.")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes= int(input("What is the total votes in the election? "))
#percentage_votes= (my_votes/total_votes)*100
#print(f"I received {my_votes/total_votes*100}% of the total votes.")

for county, voters in counties_dict.items():
    print(county, "county has ",voters, "registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#candidate_votes= int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes:,} number of votes. " 
 #   f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes. ")
#print(message_to_candidate)

for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters. ")

#for counties_dict in voting_data:
#    for value in counties_dict:
#        for keys in counties_dict:
#            print(f"{'keys'} county has {'value':,} registered voters. ")


#testing if this updates to git bash

  