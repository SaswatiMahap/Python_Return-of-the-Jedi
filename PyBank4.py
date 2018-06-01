import os
import csv
import array
import pandas as pd


# filepath = os.path.join("budget_data_1.csv")
# filepath2= os.path.join("budget_data_2.csv")

a = pd.read_csv("budget_data_1.csv")
b = pd.read_csv("budget_data_2.csv")
all = pd.concat([a,b])
print(all)

# merged dictrinary 
dict_of_lists = {}
for column_name in all.columns:
    temp_list = all[column_name].tolist()
    dict_of_lists[column_name] = temp_list

#print (dict_of_lists)
e = []
e = dict_of_lists['Date']
print(e)

# The total number of months included in the dataset
e = []
e = dict_of_lists['Date']
#print(e)

count = 0

for value in e:
    count +=1   
print(count)

#The total amount of revenue gained over the entire period

f = []
f = dict_of_lists['Revenue']
print(f)

total = 0

for value in f:
    total = sum(f)
print(total)


# #The average change in revenue between months over the entire period

diff = 0
avg = 0

for value in f:
    if (value == f[0]): 
        diff = 0
        counter=0
    else: 
        counter+=1
        diff+=f[counter]-f[counter-1]

avg = (diff/(counter-1))

print(avg)


# The greatest increase in revenue (date and amount) over the entire period
print (a)
dict2 = {}
for column_name in a.columns:
    temp_list = a[column_name].tolist()
    dict2[column_name] = temp_list
# print(dict2)

z = []
z = dict2['Revenue']
print(z)

minval = 0 
minval = z.index(min(z))
maxval = 0
maxval = z.index(max(z))

print (maxval)
print (minval)
print(f'{dict2["Date"][maxval]} has the greatest revenue {dict2["Revenue"][maxval]}')

    
#The greatest decrease in revenue (date and amount) over the entire period


print(f'{dict_of_lists["Date"][minval]} has the least revenue {dict_of_lists["Revenue"][minval]}')

# In addition, your final script should both print the analysis to the terminal and export a text file with the results
f = open("PyBank.txt", "w")
print(('The total months:',count), file=f)
print(total, file=f)
print(avg,file=f)
print((f'{dict2["Date"][maxval]} has the greatest revenue {dict2["Revenue"][maxval]}'), file=f)
print((f'{dict_of_lists["Date"][minval]} has the least revenue {dict_of_lists["Revenue"][minval]}'), file=f)
f.close()
