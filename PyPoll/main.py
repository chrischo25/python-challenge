# import
import csv
import pathlib

# Set file path
pypoll_file = pathlib.Path("election_data.csv")

# Set up lists
khan_count = []
correy_count = []
li_count = []
otooley_count = []

# Set up dictionary to loop through

# Set up variables
total_votes = 0

# Open PyPoll file
with open (pypoll_file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Calculate total number of votes
    for rows in csvreader:
        total_votes = total_votes + 1

        # Check if names are in the row, add to separate list
        if rows[2] == "Khan":
            khan_count.append(rows[2])

        elif rows[2] == "Correy":
                correy_count.append(rows[2])

        elif rows[2] == "Li":
                li_count.append(rows[2])

        elif rows[2] == "O'Tooley":
                otooley_count.append(rows[2])

    # Set variables for percentages
    khan_percentage = int(len(khan_count))/total_votes
    formatted_khan_percentage = format(khan_percentage,".3%")

    correy_percentage = int(len(correy_count))/total_votes
    formatted_correy_percentage = format(correy_percentage,".3%")

    li_percentage = int(len(li_count))/total_votes
    formatted_li_percentage = format(li_percentage,".3%")

    otooley_percentage = int(len(otooley_count))/total_votes
    formatted_otooley_percentage = format(otooley_percentage,".3%")

    # reate dictionary to determine winner
    khan_total = len(khan_count)
    correy_total = len(correy_count)
    li_total = len(li_count)
    otooley_total = len(otooley_count)
    winner = {"Khan":khan_total,"Correy":correy_total,"Li":li_total,"O'Tooley":otooley_total}
    max_winner = max(winner, key=winner.get)

    # Print Election results
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("---------------------------")
    print(f"Khan: {formatted_khan_percentage} ({khan_total})")
    print(f"Correy: {formatted_correy_percentage} ({correy_total})")
    print(f"Li: {formatted_li_percentage} ({li_total})")
    print(f"O'Tooley: {formatted_otooley_percentage} ({otooley_total})")
    print("---------------------------")
    print(f"Winner: {max_winner}")
    print("---------------------------")

# Output to CSV
output_path = pathlib.Path("output_pypoll.csv")

with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes: ",str(total_votes)])
    csvwriter.writerow(["Khan: ",formatted_khan_percentage,khan_total])
    csvwriter.writerow(["Correy: ",formatted_correy_percentage,correy_total])
    csvwriter.writerow(["Li: ",formatted_li_percentage,li_total])
    csvwriter.writerow(["O'Tooley: ",formatted_otooley_percentage,otooley_total])
    csvwriter.writerow(["Winner: ",max_winner])
    

