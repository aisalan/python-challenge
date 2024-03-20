import os
import csv

PyBankcsv = os.path.join(".", "budget_data.csv")
output_file = "financial_analysis.txt"

total_months = 0
net_total = 0
profit_losses = []
dates = []

data = []
with open(PyBankcsv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        profit_losses.append(int(row[1]))
        dates.append(row[0])

        changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]
average_change = sum(changes) / len(changes)

greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}")
with open(output_file, "w") as txtfile:
    # Write the calculation results to the file
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print confirmation message
print(f"Financial analysis results have been exported to '{output_file}'.")
