import os
import csv

# Csv path for location 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initilizing the variables
total_months = 0
total_profit_loses = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# path to perform calculations 
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months +=1
        total_profit_loses += profit_loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}
            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}
        previous_profit_loss = profit_loss

# average calc and other metrics 
average_change = sum(changes) / len(changes) if changes else 0

# test print 
print("Hello World")
    
# calculations for PyBank
print("Financial Analysis for PyBank:")
print("--------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loses}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: (${greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: (${greatest_decrease['date']} (${greatest_decrease['amount']})")

# File export 
results_path = os.path.join('analysis', 'financial_analysis.txt')
with open(results_path, mode='w') as file:
    file.write("Financial Analysis for PyBank\n")
    file.write("--------")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loses}\n")
    file.write(f"Average Change: ${average_change: .2f}\n")
    file.write(f"Greatest Increase in Profits: (${greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: (${greatest_decrease['date']} (${greatest_decrease['amount']})\n")
