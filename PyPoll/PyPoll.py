# imports necessary modules for my code
import os, csv

# sets up a path to the data file
election_data = os.path.join('python-challenge','PyPoll','election_data.csv')

#variables to be used later
total_votes_list = []
candidate = []
vote = []
candidate_votes_dict= {}


with open(election_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    election_data_list = csvreader

    # this loop will run through each row in the csv file 
    for row in election_data_list:

        # This will take all the votes and add them to the list total_votes_list.   I did this to get the total number of votes for all the canidates (len(total_votes_list))
        total_votes_list.append(row[0])

        # This will add the name from each row each iteration to be evaluated in my if statement later.  Same for the vote variable.
        candidate = row[2]
        vote = row[0]

        # if candidate name has already been added to the dictionary as a list then add the value associated with the candidate to the candidate which is now a key in the dictionary
        if candidate not in candidate_votes_dict:

            # if the candidates name hasn't been made a key yet, it then sets the new candidate to be a key for the dictionary
            candidate_votes_dict[candidate] = []

        #  This last bit of code finally takes the values that are associated with each of the candidates (this case vote numbers) and assigns them to the candidate that won that vote
        candidate_votes_dict[candidate].append(vote)

# From my dictionary now assign each of my keys their own individual variables so I can print them out later
total_votes = len(total_votes_list)
first_candidate = list(candidate_votes_dict.keys())[0]
second_candidate = list(candidate_votes_dict.keys())[1]
third_candidate = list(candidate_votes_dict.keys())[2]

# Tallied the votes for each candidate
first_candidate_votes = (len(candidate_votes_dict[first_candidate]))
second_candidate_votes = (len(candidate_votes_dict[second_candidate]))
third_candidate_votes = (len(candidate_votes_dict[third_candidate]))

# Calculated the % values for each candidate
first_candidate_pervotes = round((first_candidate_votes/total_votes) *100 , 3)
second_candidate_pervotes = round((second_candidate_votes/total_votes) *100, 3)
third_candidate_pervotes = round((third_candidate_votes/total_votes) *100, 3)
                       

print("Election results \n------------------------------------------")
print(f"Total Votes: {len(total_votes_list)} \n------------------------------------------")
print(f"{first_candidate}: {first_candidate_pervotes}% ({first_candidate_votes}) \n{second_candidate}: {second_candidate_pervotes}% ({second_candidate_votes}) \n{third_candidate}: {third_candidate_pervotes}% ({third_candidate_votes}) \n------------------------------------------")
print(f"Winner: {second_candidate}")

output_file = os.path.join("PyPoll","PyPoll_Final.txt")
with open("PyPoll_Final.txt", "w") as text:
    text.write("Election results\n")
    text.write("------------------------------------------\n")
    text.write(f"Total Votes: {len(total_votes_list)}\n")
    text.write("------------------------------------------\n")  
    text.write(f"{first_candidate}: {first_candidate_pervotes}% ({first_candidate_votes}) \n{second_candidate}: {second_candidate_pervotes}% ({second_candidate_votes}) \n{third_candidate}: {third_candidate_pervotes}% ({third_candidate_votes}) \n------------------------------------------\n")
    text.write(f"Winner: {second_candidate}")
text.close()
