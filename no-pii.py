# importing dependencies
import csv
import sys
import os
import pandas
import scrubadub
import datasync
import time

dirty_data = ['Activity_Age_Gender', 'Activity Listing Report_11-08-04 AM_11088', 'Activity Section Listing Segments By Subtype_11-05-29 AM_11124', 'Activity Visit Report_11-02-25 AM_5052',
'Pass Type Summary Visit Report_ 1-31-46 PM_2076', 'Athletics HH Reservation Report_12-37-07 PM_5808', 'Facility Class Listing Report_12-44-08 PM_6628', 'Facility Location Listing Report_12-40-42 PM_6292',
'Global Cancellation Report_11-28-25 AM_7844', 'permitsjan23', 'Global Trial Balance Summary - HH Net Balance_12-13-54 PM_8708', 'Pass Bottom Line Report_11-56-49 AM_9052', 'PASS MEMBER W AGE _11-45-45 AM_8708',
'Refund Detail Report_11-31-42 AM_10244', 'User Listing Report_10-09-52 AM_6780']

check_list = ['Email', 'Emails', 'Name', 'Names', 'Credit Card', 'Phone Number', 'Phone', 'Telephone',
'Credit Card Number', 'Email Address', 'Address', 'Street Address', 'First Name', 'Last Name', 'PIN Number', 'PIN',
'Member Name', 'Pass #', 'Pass Code', 'Fees/Tax', 'Amt Paid', 'Age', 'Full Name', 'Household #', 'Item Code',
'Member', 'Amount', 'User Name', 'Primary Contact', 'Email Address', 'Primary Guardian', 'Enrollee', 'Household'
'Property Owner', 'Property Address', 'Contractor Contact Details', 'Contractors']

to_drop = []

# select file to open, display data in command line
def findFile():
    for i in dirty_data:
        fileName = i
        print(os.path.abspath("../datasets/" + fileName) + ".csv")
        df = pandas.read_csv(os.path.abspath("../remove-pii/datasets/" + fileName) + ".csv", error_bad_lines=False, encoding='latin_1')
        print("===============================")
        confirmDelete(df, fileName)

# checks with user to confirm if more rows need cleaning
def checkFinished(df, fileName):
    print("============================================================")
    df.to_csv(fileName + "_scrubbed.csv", encoding='utf-8', index = False)
    print('Scrubbed file complete.')
    print("===============================")
    dirty_data.pop(0)
    findFile()

# scrubs the data from the chosen column
# only does one at a time, working on improving that
def scrubData(df, fileName):
    print("===============================")
    print("Scrubbing data... (larger datasets can take time)")
    print("===============================")
    # line 41 does all the work
    df.drop(to_drop, axis=1, inplace=True)
    to_drop.clear()
    checkFinished(df, fileName)

# iterates over list of common PII and compares against the names of column headers
# in a given .csv.  If there are any matches, those matches populate the "to_drop" list
def confirmDelete(df, fileName):
    for column in df:
        for i in check_list:
            if i == column:
                to_drop.append(i)
    print('Here are the Column headers that will be searched for: ')
    print(to_drop)
    scrubData(df, fileName)

# calls confirmDelete function
findFile()