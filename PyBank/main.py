import csv
from pathlib import Path
csv_path = Path('budget_data.csv')

total_months = 0
records = {}
pnls = []
deltas = []
total_pnl = 0
total_months = 0

total_months = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    
    # Read each row of data after the header
    for row in csv_reader:
        month = row[0]
        pnl = int(row[1])
        total_pnl += pnl
        total_months += 1
        pnls.append(pnl)
        
        if total_months < 2:
            delta = 0
        else:
            delta = pnls[total_months-1] - pnls[total_months-2]
            deltas.append(delta)
            
        records.update({delta: month})
    
increase = max(deltas)
decrease = min(deltas)
avg_changes = round(sum(deltas)/(total_months-1),2)

print('Financial Analysis')
print('-----------------------')
print(f'Total Months: {total_months}')
print(f'Total: $ {total_pnl}')
print(f'Average Change: ${avg_changes}')
print(f'Greatest Increase in Profits: {records[increase]} (${increase})')
print(f'Greatest Decrease in Profits: {records[decrease]} (${decrease})')







