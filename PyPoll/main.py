# Dependencies (library)
import os
import csv

# open csv file and confirm path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources\election_data.csv')

# open csv file and confirm path
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents (optimize reader)
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first -- confirms file has header
    csv_header = next(csvreader)
    first_row = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print(" ")

    # initialize variables
    total_votes = 1
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    row = 0
    sort_list = []

    # Read each row of data after the header
    for row in csvreader:
        total_votes +=1
        voter_cast = str(row[2])
        if(voter_cast == "Khan"):
            khan_votes +=1
        elif(voter_cast == "Correy"):
            correy_votes +=1
        elif(voter_cast == "Li"):
            li_votes +=1
        elif(voter_cast == "O'Tooley"):
            otooley_votes +=1

khan_pct_votes = ((int(khan_votes)/int(total_votes))*100)
correy_pct_votes = ((int(correy_votes)/int(total_votes))*100)
li_pct_votes = ((int(li_votes)/int(total_votes))*100)
otooley_pct_votes = ((int(otooley_votes)/int(total_votes))*100)
sort_list = [[khan_votes,"Khan"], [correy_votes,"Correy"], [li_votes,"Li"], [otooley_votes,"O'tooley"]]
sort_list.sort(reverse = True)
winner_name = sort_list[0]

# print results to the terminal
print(" ")
print("      Election Results")
print("-----------------------------")
print("Total Votes:          " + str(int(total_votes)))
print("-----------------------------")
print("   Khan:     " + str("{:.3f}".format(khan_pct_votes)) + "%" + "  " + str(int(khan_votes)))
print("   Correy:   " + str("{:.3f}".format(correy_pct_votes)) + "%" + "  " + str(int(correy_votes)))
print("   Li:       " + str("{:.3f}".format(li_pct_votes)) + "%" + "  " + str(int(li_votes)))
print("   O'Tooley:  " + str("{:.3f}".format(otooley_pct_votes)) + "%" + "  " + str(int(otooley_votes)))
print("-----------------------------")
print("Winner:       " + str(winner_name[1]))
print("-----------------------------")
print(" ")

# Write the election results to a text file
# Specify the file to write to
os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Output Data\PyPoll_main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows to text file - 
    csvwriter.writerow([' '])
    csvwriter.writerow(['     Election Results'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow(['Total Votes:          ' + str(int(total_votes))])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow(['   Khan:     ' + str("{:.3f}".format(khan_pct_votes)) + '%' + '  ' + str(int(khan_votes))])
    csvwriter.writerow(['   Correy:   ' + str("{:.3f}".format(correy_pct_votes)) + '%' + '  ' + str(int(correy_votes))])
    csvwriter.writerow(['   Li:       ' + str("{:.3f}".format(li_pct_votes)) + '%' + '  ' + str(int(li_votes))])
    csvwriter.writerow(['   O Tooley:  ' + str("{:.3f}".format(otooley_pct_votes)) + '%' + '  ' + str(int(otooley_votes))])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow(['Winner:       ' + str(winner_name[1])])
    csvwriter.writerow(['-----------------------------'])


