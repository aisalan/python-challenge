#dependencies
import os
import csv

#define the file path
PyBankcsv = os.path.join(".", "budget_data.csv")


#variables
total_months = 0
net_total = 0
profit_losses = []
dates = []

#load the data from the csv file
data = []
with open(PyBankcsv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #iteration
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        profit_losses.append(int(row[1]))
        dates.append(row[0])

#track the monthly changes
        changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]
average_change = sum(changes) / len(changes)

greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

#calculation
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}")