#import 
import csv
import os

#define file
csv_file=os.path.join("Resources","budget_data.csv")
#define txt file
txt_file=os.path.join("Analysis", "budget_analysis.txt")
#tracking/define variables
total_months=0
net_change_list=[]
greatest_increase=["", 0]
greatest_decrease=["", 9999999999]
#read in csv file and convert to dict.
with open(csv_file) as budget_data:
    reader=csv.reader(budget_data)
     #read in title row of csv
    header=next(reader)
     #extract 1st row of data**
    first_row=next(reader)
    total_months+=1
    total_net=int(first_row[1])
    previous_net=int(first_row[1])
    

     #create forloop: track total, track change, greatest increase/decrease*
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[0])

        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        


#Average monthly change
net_monthly_average=sum(net_change_list)/len(net_change_list)
#generate and print output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n")
    # f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    # f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
#export results to txt file
with open(txt_file, "w") as budget_analysis:
    budget_analysis.write(output)