# Set up imports
import pathlib
import csv
import itertools

# Set up file paths
pybank_csv = pathlib.Path("budget_data.csv")

# Create lists
months = []
profits = []
monthly_change = []
pybank_dictionary = {}

# Open the CSV file
with open (pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Loop through the csv file
    for rows in csvreader:
        
        # Append all months and profits into separate lists
        months.append(rows[0])
        profits.append(int(rows[1]))

        
    # Loop through profits list to calculate average of the changes
    for x in range(len(profits)-1):
        monthly_change.append(profits[x+1]-profits[x])

# Create a list starting from Feb 2010
months_plus_one=months[1:]

# Calculate average monthly change
average_change = round(sum(monthly_change)/len(monthly_change),2)

# Zip months list and monthly_change list into dictionary
monthly_change_dictionary = dict(zip(months_plus_one,monthly_change))

# Calculate greatest increase in profits
greatest_increase = max(monthly_change)
greatest_increase_month = max(monthly_change_dictionary,key=monthly_change_dictionary.get)


# Calculate greatest decrease in losses
greatest_decrease = min(monthly_change)
greatest_decrease_month = min(monthly_change_dictionary,key=monthly_change_dictionary.get)
   


# Print out financial statement
print("Financial Analysis")
print("-----------------------------")
print(f"Total months: {str(len(months))}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Output files to CSV
output_path = pathlib.Path("output_pybank.csv")

with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total months: ",str(len(months))])
    csvwriter.writerow(["Total: ",sum(profits)])
    csvwriter.writerow(["Average Change: ",average_change])
    csvwriter.writerow([f"Greatest Increase in Profits: ",f"{greatest_increase_month} ({greatest_increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: ",f"{greatest_decrease_month} ({greatest_decrease})"])    

