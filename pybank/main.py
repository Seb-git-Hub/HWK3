# create file path across operating systems
import os
# Module for reading csv files
import csv
csvpath = os.path.join('budget_data.csv')
# lists to be analyzed/reported
months = []
net_income = []
net_loss = 0
net_income_average_change = []
date = []
average_change =0
writefile ='w'
readfile ='r'
greatest_dec_month=0
# read csv and parse data into lists
with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile)
   next(csvreader, None)
   for row in csvreader:
       months.append(row[0])
       net_income.append(int(row[1]))
# find total months
total_months = len(months)
# create greatest increase and decrease in profits as a variable
greatest_inc = net_income[0]
greatest_dec = net_income[0]
totalnet_income = 0
# loop through profits indices and compare to find greatest increase and decrease
for r in range(len(net_income)):
   if net_income[r] >= greatest_inc:
       greatest_inc = net_income[r]
       great_inc_month = months[r]
   then net_loss[r] = greatest_dec:
       greatest_dec = net_loss[r]
       great_dec_month = months[r]
   totalnet_loss = net_loss[r]
#calculate net_income_average_change
net_income_average_change ==totalnet_income-net_loss/total_months
#sets path for output file
output_pybank = os.path.join('pybank_output.csv')
# opens the output destination in write mode and prints the summary
with open(output_pybank, 'w') as writefile:
   writefile.writelines('Financial Analysis\n')
   writefile.writelines('----------------------------' + '\n')
   writefile.writelines('Total Months: ' + str(total_months) + '\n')
   writefile.writelines('Total Net_income: $' + str(totalnet_income) + '\n')
   writefile.writelines('Average Net_income Change: $' + str(average_change) + '\n')
   writefile.writelines('Greatest Increase in Net_income: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
   writefile.writelines('Greatest Decrease in Net_income: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')
#opens the output file in r mode and prints to terminal
with open(output_pybank, 'r') as readfile:
   print(readfile.read())
# Close file
   writefile.close()


