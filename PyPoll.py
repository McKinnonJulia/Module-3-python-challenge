import pandas as pd

# Load election_data
election_data = pd.read_csv('election_data.csv')

# Total_votes
total_votes = election_data['Ballot ID'].count()

# total votes for candidate
candidate_votes = election_data['Candidate'].value_counts()

# votes percentage_candidates won
candidate_percentage = (candidate_votes / total_votes) * 100

# Find winner
winner = candidate_votes.idxmax()
winner_votes = candidate_votes.max()

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open('election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")