import os
import csv
election_data_file = os.path.join("Resources","election_data.csv")

#defining variables
total_votes = []
candidates = []
candidate_list = []
Raymon=[]
candid_2=[]
candid_3=[]
candidate_votes={}


#reading the csv file
with open(election_data_file) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csvheader = next(csv_reader)
    data = list(csv_reader)
    
    #calculating the total votes
    for row in data:
        total_votes.append(row[0])


#printing to terminal
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {len(total_votes)}")
print(f"-----------------------")




#printing to .txt file
f=open("output",mode="wt")
f.write("Election Results" + "\n")
f.write("-----------------------" + "\n")
f.write("Total Votes: " + str(len(total_votes)) + "\n")
f.write("-----------------------" + "\n")
f.close()




  