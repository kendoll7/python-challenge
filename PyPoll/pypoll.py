#!/usr/bin/env python
# coding: utf-8

# In[66]:


import os
import csv

election_data_csv = os.path.join(".", "Resources", "election_data.csv")

output_text_file = os.path.join(".", "election_results.txt")

#Variables List
total_votes = 0

candidate_votes = {}
candidate_choices = []

winning_candidate = ""
winning_count = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
       
    header = next(csvreader)
    #print(header)
    
    for row in csvreader:
        #add 1 to each vote count
        total_votes += 1
        
        #Get the candidate name from each row
        candidate_name = row[2]
        
        #Go through each candidate name
        if candidate_name not in candidate_choices:
            
            #If a name is not in the list, add them to the list
            candidate_choices.append(candidate_name)
            
            #Take that name and put them at 0 votes
            candidate_votes[candidate_name]= 0
        #add a vote every time that name appears, until we reach a different candidate name
        candidate_votes[candidate_name] += 1
        
#print(candidate_votes)       
#print(candidate_choices)
#print(total_votes)    
    
    
with open(output_text_file, "w") as txt_file:
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
       
    )
    print(output)
    
    txt_file.write(output)
   
    #for each amount of votes per candidate
    for candidate in candidate_votes:
        #take the votes of the candidate
        votes = candidate_votes[candidate]
        #calculate the vote percentage
        votes_percentage = float(votes) / float(total_votes) * 100
        
        #print(votes)
        #print(votes_percentage)
        
        #print the output in the desired format
        voter_output = (f"{candidate}: {votes_percentage:.3f}% ({votes})\n")
        print(voter_output)
    
        txt_file.write(voter_output)
        
        #if the number of votes exceed the winning count per candidate
        if (votes> winning_count):
            winning_count = votes
            winning_candidate = candidate
        
    winning_candidate_result = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------"
        )
    print(winning_candidate_result)
    txt_file.write(winning_candidate_result)


# In[ ]:




