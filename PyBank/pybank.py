#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

pybank_csv = os.path.join(".", "Resources", "budget_data.csv")

output_text_file = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_dollars = 0
total_net = 0
net_change_list = []
average_change = 0
month_of_change_list = []

total_months += 1


#First entry is month, second entry is 0 because greatest must be greater than 0
greatest_list = ["", 0]
#First entry is month, second entry is 0 because greatest must be less than 0
least_list = ["", -1]

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header when counting
    header = next(csvreader)

    first_row = next(csvreader)
    
    total_dollars = int(first_row[1])
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    #print(total_net)
    #print(previous_net)
    
    for row in csvreader:
        #print(row)
        
        #Add +1 to the total months for each row
        total_months = total_months + 1
        
        #Add to the row above it
        total_dollars = total_dollars + int(row[1])
        
        #Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        
        #Add the net changes per each row to a list
        net_change_list.append(net_change)
        
        month_of_change_list.append(row[0])
        
        #Calculating the greatest number)
        #if the net change is greater than our greatest number
        if(net_change > greatest_list[1]):
            #save the month of the change
            greatest_list[0] = row[0]
            #add the net change as the greatest number
            greatest_list[1] = net_change
        
        #Calculating the greatest number)
        #if the net change is greater than our greatest number
        if(net_change < least_list[1]):
            #save the month of the change
            least_list[0] = row[0]
            #add the net change as the greatest number
            least_list[1] = net_change
        
#print(net_change_list)
average_change = sum(net_change_list) / len(net_change_list)

#print(month_of_change_list)

#use this for max, and corresponding min statement
#print(max(net_change_list))

#print results
#("Total Months: " + str(total_months))
#("Total: $" + str(total_dollars))
#("Average Change: $" + str(round(average_change, 2)))
#("Greatest Increase in Profits: " + str(greatest_list[0]) + " ($" + str(greatest_list[1]) +")" )
#("Greatest Decrease in Profits: " + str(least_list[0]) + " ($" + str(least_list[1]) + ")" )
output = (
    f"Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_dollars}\n"
    f"Average Change: ${round(average_change, 2)}\n"
    f"Greatest Increase in Profits: {greatest_list[0]} (${greatest_list[1]})\n"
    f"Greatest Decrease in Profits: {least_list[0]} (${least_list[1]})\n"
)

print(output)

with open(output_text_file, "w") as txt_file:
    txt_file.write (str(output))

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# In[ ]:





# In[ ]:




