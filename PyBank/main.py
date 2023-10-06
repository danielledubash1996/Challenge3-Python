import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")
total_months = []
total_profits = []
change_in_profit = []


#reading file and getting the necessary data
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header=next(csv_file)
    
    #using the following equations in a for loop to begin calculating
    for row in csv_reader:
        total_months.append(row[0])
        total_profits.append(int(row[1]))
    
    for x in range(1,len(total_profits)):
        change_in_profit.append((int(total_profits[x])) - int(total_profits[x-1]))

    average_change=(sum(change_in_profit))/(len(change_in_profit))
   
    greatest_increase = max(change_in_profit)
    greatest_decrease = min(change_in_profit)

    print ("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profits)}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: ${greatest_increase}")
    print(f"Greatest Decrease in Profits: ${greatest_decrease}")


file = open("output.txt",mode="wt")
file.write("Financial Analysis" + "\n")
file.write("----------------------" +"\n")
file.write("Total Months: $" + str(len(total_months)) + "\n")
file.write("Total: $"+ str(sum(total_profits)) + "\n")
file.write("Average Change: $" + str(round(average_change,2)) + "\n")
file.write("Greatest Increase in Profits: $" + str(greatest_increase) + "\n")
file.write("Greatest Decrease in Profits: $" + str(greatest_decrease) + "\n")
file.close()
