# importing dependencies
import csv
import sys
import os
import pandas
import scrubadub
import datasync

# select file to open, display data in command line
fileName = input("What's the name of the desired file? ")
df = pandas.read_csv(fileName + ".csv")
df.head(n=5)
print(df)

# checks with user to confirm if more rows need cleaning
def checkFinished():
    yesNo = input("Column cleaned. Would you like to scrub another column? ")
    if yesNo == 'yes':
        scrubData()
    else:
        # writes new .csv file  
        df.to_csv(fileName + "_scrubbed.csv", encoding='utf-8', index = False)
        print('Scrubbed file complete.')

# scrubs the data from the chosen column
# only does one at a time, working on improving that
def scrubData():
    columnName = input("Which columns would you like to delete? ")
    print("Scrubbing data... (larger datasets take time)")
    scrub = lambda x: scrubadub.clean(' ')
    df[str(columnName)] = df[str(columnName)].apply(scrub)
    checkFinished()

# calls scrubData function
scrubData()