# import the os (library) module to create file paths across operating systems
import os

# import CSV file reader - open path C:\PythonHW\python-challenge\PyBank
import csv

# open csv file and confirm path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('budget_data.csv')
# print(csvpath)
# open budget_data.csv file
# open csv file and confirm path
with open(csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents (optimize reader)
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # Read the header row first -- confirms file has header
    csv_header = next(csvreader)
    first_row = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(" ")

    # initialize variables
    total_rows = 1
    total_margin = 0
    prior_mo_mrgn = int(first_row[1])
    greatest_profit_inc_mo = 0
    greatest_profit_inc_amt = 0
    greatest_profit_dec_mo = 0
    greatest_profit_dec_amt = 0

    #define list variable
    Ave_change = []
    greatest_profits = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999999999999999]

# Read each row of data after the header
    for row in csvreader:
        total_rows +=1
        profit_loss = int(row[1])
        total_margin += profit_loss
        monthly_chg = int(row[1])-prior_mo_mrgn
        prior_mo_mrgn = int(row[1])
        Ave_change.append(monthly_chg)

        if profit_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss
        if profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss

# Calculate for the average monthly change in Profit/Losses           
average_mo_chg = round(sum(Ave_change)/len(Ave_change),2)

# print the summary of results
print("Financial Analysis")
print("-------------------------------------")
print("Total Months:     " + str(int(total_rows)))
print("Total:           " + str("${:.0f}".format(total_margin)))
print("Average Change:  " + str("${:.2f}".format(average_mo_chg)))
greatest_profit_inc_mo = greatest_increase[0]
greatest_profit_inc_amt = (greatest_increase[-1])
print("Greatest Increase in Profits: " + str(greatest_profit_inc_mo) + "   " + str("${:.0f}".format(greatest_profit_inc_amt)))
greatest_profit_dec_mo = greatest_decrease[0]
greatest_profit_dec_amt = greatest_decrease[-1]
print("Greatest Decrease in Profits: " + str(greatest_profit_dec_mo) + "  " + str("${:.0f}".format(greatest_profit_dec_amt)))
print(" ")

# Write the election results to a text file
# Specify the file to write to
os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("PyBank_main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows to text file - 
    csvwriter.writerow([' '])
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------'])
    csvwriter.writerow(['Total Months:     ' + str(int(total_rows))])
    csvwriter.writerow(['Total:           ' + str("${:.0f}".format(total_margin))])
    csvwriter.writerow(['Average Change:  ' + str("${:.2f}".format(average_mo_chg))])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(greatest_profit_inc_mo) + '   ' + str("${:.0f}".format(greatest_profit_inc_amt))])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(greatest_profit_dec_mo) + '  ' + str("${:.0f}".format(greatest_profit_dec_amt))])
