# PyPoll

# Read election_data.csv
import os
import csv

csvpath =os.path.join('Documents/Data Science Bootcamp/Python-challenge/PyPoll/election_data.csv')

count=0
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    # check headers
    print(f"csv_header: {csv_header}")
    # Just look at the first 10 rows
    # reference: https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time-in-python
    lines = [i for i in csvreader][:10]
    print(lines)

# ---------------------------

# The total number of votes cast 
# reference : https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s07.html
count=0
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)    

    for line in csvreader:
        count=count+1
    # need to exclude header row 
    total_votes=count
    print(total_votes)  #1048575
  

# ---------------------------
# A complete list of candidates who received votes
# First create variables to hold voter id, counties, and counties

VoterID1=[]
County1=[]
Candidate1=[]

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    # check headers
    print(f"csv_header: {csv_header}")

    for row in csvreader:
        VoterID_t=row[0]
        County_t=row[1]
        Candidate_t=row[2]

        VoterID1.append(VoterID_t)
        County1.append(County_t)
        Candidate1.append(Candidate_t)

    print(VoterID1[0:3])
    print(County1[0:3])
    print(Candidate1[0:3])

    # index ranges from 0 to 1048575 since 1048575 is the number of voters
    Candidate_list=[]
    # Initializrd Candidate_list
    Candidate_list.append(Candidate1[0])
    print(Candidate_list)
   
   # if a candidate is not included in the Candidate_list, add the candidate to the list
    for i in range(0,1048575):
        if Candidate1[i] not in Candidate_list:
            Candidate_list.append(Candidate1[i])
    print(Candidate_list)
    #['Khan', 'Correy', 'Li', "O'Tooley"]
# ---------------------------------

# The total number of votes each candidate won
# we already know the names of the candidates
# So, count the # of appearances of each candidate name
# reference : https://medium.com/better-programming/how-to-count-occurrences-in-a-python-list-f799072538b3

Khan=Candidate1.count('Khan')
print(f"Khan has {Khan}") # Khan has 661583

Correy=Candidate1.count('Correy')
print(f"Correy has {Correy}") # 209046

Li=Candidate1.count('Li')
print(f"Li has {Li}") #  146360

Tooley = total_votes - (Khan + Correy + Li)
print(Tooley) # 31586


# The percentage of votes each candidate won
#reference https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
#reference : https://realpython.com/python-rounding/

p_khan=(Khan / total_votes)*100
print(p_khan) # 63.09353169778033
print ("{:.5}%".format(p_khan)) # 63.094%
p_khan2=("{:.5}%".format(p_khan))


p_Correy=(Correy / total_votes)*100
print(p_Correy) # 19.93619912738717
print ("{:.5}%".format(p_Correy)) # 19.936%
p_Correy2=("{:.5}%".format(p_Correy)) 

p_Li=(Li / total_votes)*100
print(p_Li) # 13.957990606299026
print ("{:.5}%".format(p_Li)) # 13.958%
p_Li2=("{:.5}%".format(p_Li))

p_Tooley=(Tooley / total_votes)*100
print(p_Tooley) # 3.0122785685334863
print ("{:.5}%".format(p_Tooley)) # 3.0123%
p_Tooley2=("{:.5}%".format(p_Tooley))
print(p_Tooley2)

# Let's save who got what % in dictionary
dict={
    "khan" : 63.09353169778033,
    "Correy" : 19.93619912738717,
    "Li" : 13.957990606299026,
    "Tooley" : 3.0122785685334863
}
print(dict)


# Other method for counting number of voters for each candidate
#Khan = [
#   number
#   for number in Candidate1
#   if number == 'Khan'
#]
#count_Khan = len(Khan)
#print(count_Khan) #661583

# --------------------------------

# The winner of the election based on popular vote.

v_percent=[p_khan, p_Li, p_Correy, p_Tooley]
print(v_percent)
win=0
for i in range(0,3):
    value=v_percent[i]
    value2=v_percent[i+1]
    if value > value2 and value>win:
        win=value
print(win)
#63.09353169778033

# reference : https://www.youtube.com/watch?v=QLEmEl7H1Ks
print ([name for name, number in dict.items() if number==63.09353169778033])
# winnter is ['khan']

