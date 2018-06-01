import os
import csv
import array
import pandas as pd


csvpath = os.path.join('election_data_1.csv')
csvpath2= os.path.join('election_data_2.csv')

#with open(cereal_csv, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")

with open(csvpath, newline="") as csvpathr:
    csvreader = csv.reader(csvpathr, delimiter=",")

    
with open(csvpath2, newline="") as csvpathr2:
    csvreader2 = csv.reader(csvpathr2, delimiter=",")

a = pd.read_csv("election_data_1.csv")
b = pd.read_csv("election_data_2.csv")
all = pd.concat([a,b])

# merged dictrinary 
dict_of_lists = {}
for column_name in all.columns:
    temp_list = all[column_name].tolist()
    dict_of_lists[column_name] = temp_list

# The total number of votes cast


#print (dict_of_lists)
e = []
e = dict_of_lists['Voter ID']


# The total number of voters  included in the dataset
count = 0

for value in e:
    count +=1   
print(count)

#A complete list of candidates who received votes
#Candidate
f = []
f = dict_of_lists['Candidate']
cand_list = set(f)
print(cand_list)

#The total number of votes each candidate won

def get_cnt(lVals):
    d = dict(zip(lVals, [0] * len(lVals)))
    for x in lVals:
        d[x] += 1
    return d

print (get_cnt(f))

dictionary = {}
dictionary = get_cnt(f)
print (dictionary)

#The percentage of votes each candidate won
#{'Li', 'Khan', 'Vestal', 'Seth', 'Correy', 'Cordin', 'Torres', "O'Tooley"}
Li = (dictionary['Li']/4324001)*100
print ("Li got the following percentage of vote: " + str(Li))

Khan = (dictionary['Khan']/4324001)*100
print ("Khan got the following percentage of vote: " + str(Khan))

Vestal = (dictionary['Vestal']/4324001)*100
print ("vestal got the following percentage of vote: " + str(Vestal))

Seth = (dictionary['Seth']/4324001)*100
print ("Seth got the following percentage of vote: " + str(Seth))

Correy = (dictionary['Correy']/4324001)*100
print ("Correy got the following percentage of vote: " + str(Correy))

Cordin = (dictionary['Cordin']/4324001)*100
print ("Cordin got the following percentage of vote: " + str(Cordin))

Torres = (dictionary['Torres']/4324001)*100
print ("Torres got the following percentage of vote: " + str(Torres))

Tooley = (dictionary["O'Tooley"]/4324001)*100
print ("Tooley got the following percentage of vote: " + str(Tooley))

# #The winner of the election based on popular vote.
# max_val = 0 
# max_val == 0

# For key in dictionary.keys():
#     if dictionary[]> max_val:
#         max.candidate = key 
#         max_val = dict[key]

import operator
print ('Winner of the election is:', max(dictionary.items(), key=operator.itemgetter(1))[0])


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
f = open("PyPoll.txt", "w")
print(('The total number of voters  included in the dataset:',count), file=f)
print(('List of candidates:', cand_list), file=f)
print ((dictionary), file=f)
print (("Li got the following percentage of vote: " + str(Li)), file=f)
print (("Khan got the following percentage of vote: " + str(Khan)), file=f)
print (("vestal got the following percentage of vote: " + str(Vestal)), file=f)
print (("Seth got the following percentage of vote: " + str(Seth)), file=f)
print (("Correy got the following percentage of vote: " + str(Correy)),file=f)
print (("Cordin got the following percentage of vote: " + str(Cordin)),file=f)
print (("Torres got the following percentage of vote: " + str(Torres)),file=f)
print (("Tooley got the following percentage of vote: " + str(Tooley)),file=f)
print (('Winner of the election is:', max(dictionary.items(), key=operator.itemgetter(1))[0]),file=f)
f.close()
