# importing dependencies
import csv
import sys
import os
import pandas
import scrubadub
import datasync

# select file to open, display data in command line
fileName = input("What's the name of the desired file? (Don't include file type): ")
df = pandas.read_csv(fileName + ".csv")
print(df)
# my attempt at listing off common PII label
check_list = ['Email', 'Emails', 'Name', 'Names', 'Credit Card', 'Phone Number', 'Phone', 'Telephone',
'Credit Card Number', 'Email Address', 'Address', 'Street Address', 'First Name', 'Last Name', 'PIN Number', 'PIN']
to_drop = []
print("===============================")

# checks with user to confirm if more rows need cleaning
def checkFinished():
    print(df)
    fin = input("Finished with this file? (yes/no) ")
    print("============================================================")
    if fin == 'yes' or yesNo == 'Yes':
        # writes a new "scrubbed" file
        df.to_csv(fileName + "_scrubbed.csv", encoding='utf-8', index = False)
        print('Scrubbed file complete.')
        print("===============================")
    elif fin == 'no' or fin == 'No':
        # clears list a brings program back to input stage 
        to_drop = list()
        confirmDelete()

# scrubs the data from the chosen column
# only does one at a time, working on improving that
def scrubData():
    print("===============================")
    print("Scrubbing data... (larger datasets can take time)")
    print("===============================")
    # line 41 does all the work
    df.drop(to_drop, axis=1, inplace=True)
    checkFinished()

# iterates over list of common PII and compares against the names of column headers
# in a given .csv.  If there are any matches, those matches populate the "to_drop" list
def confirmDelete():
    for column in df:
        for i in check_list:
            if i == column:
                to_drop.append(i)
    print('Here are the Column headers that will be searched for: ')
    print(to_drop)
    customizeSearch()

# in the likely event that the search doesn't recognize all the columns that contain PII
# this function allows the user to add custom entries to the "to_drop" list
def customizeSearch():
    yesNo = input("Would you like to remove an additional column? (yes/no): ")
    if yesNo == 'yes' or yesNo == 'Yes':
        columnName = input("What is the column header? (Case Sensitive): ")
        to_drop.append(columnName)
        customizeSearch()
    elif yesNo == 'no' or yesNo == 'No':
        scrubData()

# calls confirmDelete function
confirmDelete()