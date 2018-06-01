import os
import csv
import array
import pandas as pd

# # * Import the `employee_data1.csv` and `employee_data2.csv` files,
# #  which currently holds employee records like the below:

csvpath = os.path.join("employee_data1.csv")
csvpath2= os.path.join("employee_data2.csv")

with open(csvpath, newline='') as csvfile:

#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    us_state_abbrev={}
    for row in csvreader:
        print(row)
        first_name, last_name = row[1].split(" ", 1)
        print (first_name)
        print (last_name)
    #The `SSN` data should be re-written such that the first five numbers are hidden from view.
        ssn1,ssn2,ssn3 = row[3].split("-",2)
        print(ssn3)
        ssn_new=("****-**-"+ssn3)
        print(ssn_new)

    # #   * The `DOB` data should be re-written into `MM/DD/YYYY` format.
        from datetime import datetime
        new_date = row[3].strftime("%Y-%m")
        print (new_date)
    

#  * The `State` data should be re-written as simple two-letter abbreviations.

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



# #* The `Name` column should be split into separate `First Name` and `Last Name` columns.
    
# FirstName = [i.split(" ", 1)[0] for i in Name]
# print (FirstName)
    

# LastName = [i.split(" ", 1)[1] for i in Name]
# print (LastName)

# #-------------
# # a = pd.read_csv("employee_data1.csv")
# # b = pd.read_csv("employee_data2.csv")
# # all = pd.concat([a,b])
# # dict_of_lists = {}

# # for column_name in all.columns:
# #     temp_list = all[column_name].tolist()
# #     dict_of_lists[column_name] = temp_list

# # The total number of votes cast


# #print (dict_of_lists)
# # emp = []
# # emp = dict_of_lists['Emp ID']

# #* The `Name` column should be split into separate `First Name` and `Last Name` columns.

# Name = []
# Name = dict_of_lists['Name']
# # print (Name)

# FirstName = [i.split(" ", 1)[0] for i in Name]
# print (FirstName)
    

# LastName = [i.split(" ", 1)[1] for i in Name]
# print (LastName)


# #   * The `DOB` data should be re-written into `MM/DD/YYYY` format.

# DOB = []
# DOB = dict_of_lists['DOB']
# # DOB_Changed = []
# # for date in DOB:
# #     DOB_Changed.append(DOB_Changed.date(MM,DD,YYYY))
# #     print (DOB_Changed)
# # * The `SSN` data should be re-written such that the first five numbers are hidden from view.

# # SSN = []
# # SSN = dict_of_lists['SSN']
# # SSN_Changed =[]
# # SSN_Changed = [i.split("-", 1)[2] for i in Name]
# # print (SSN_Changed)


# #  * The `State` data should be re-written as simple two-letter abbreviations.

# State = []
# State = dict_of_lists['State']
# print (State)

# us_state_abbrev = {}
# us_state_abbrev = {'AK': 'Alaska',
#         'AL': 'Alabama',
#         'AR': 'Arkansas',
#         'AS': 'American Samoa',
#         'AZ': 'Arizona',
#         'CA': 'California',
#         'CO': 'Colorado',
#         'CT': 'Connecticut',
#         'DC': 'District of Columbia',
#         'DE': 'Delaware',
#         'FL': 'Florida',
#         'GA': 'Georgia',
#         'GU': 'Guam',
#         'HI': 'Hawaii',
#         'IA': 'Iowa',
#         'ID': 'Idaho',
#         'IL': 'Illinois',
#         'IN': 'Indiana',
#         'KS': 'Kansas',
#         'KY': 'Kentucky',
#         'LA': 'Louisiana',
#         'MA': 'Massachusetts',
#         'MD': 'Maryland',
#         'ME': 'Maine',
#         'MI': 'Michigan',
#         'MN': 'Minnesota',
#         'MO': 'Missouri',
#         'MP': 'Northern Mariana Islands',
#         'MS': 'Mississippi',
#         'MT': 'Montana',
#         'NA': 'National',
#         'NC': 'North Carolina',
#         'ND': 'North Dakota',
#         'NE': 'Nebraska',
#         'NH': 'New Hampshire',
#         'NJ': 'New Jersey',
#         'NM': 'New Mexico',
#         'NV': 'Nevada',
#         'NY': 'New York',
#         'OH': 'Ohio',
#         'OK': 'Oklahoma',
#         'OR': 'Oregon',
#         'PA': 'Pennsylvania',
#         'PR': 'Puerto Rico',
#         'RI': 'Rhode Island',
#         'SC': 'South Carolina',
#         'SD': 'South Dakota',
#         'TN': 'Tennessee',
#         'TX': 'Texas',
#         'UT': 'Utah',
#         'VA': 'Virginia',
#         'VI': 'Virgin Islands',
#         'VT': 'Vermont',
#         'WA': 'Washington',
#         'WI': 'Wisconsin',
#         'WV': 'West Virginia',
#         'WY': 'Wyoming'
# }


# # # Then convert and export the data to use the following format instead


# #----------------------------------------------
# # # Emp ID,Name,DOB,SSN,State
# # # 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# # # 15,
# # # Samantha Lara,1993-09-08,848-80-7526,Colorado
# # # 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# # # ```

# # #---------------------------------------------#


# # # Emp ID,First Name,Last Name,DOB,SSN,State
# # # 214,Sarah,Simpson,12/04/1985,***-


# # **-8166,FL
# # 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# # 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# # ```

# # * In summary, the required conversions are as follows:

  
# # 



  

 


# # * Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations]
# # (https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

