import csv
import sys
import os
import pandas

# select file to open, display data in command line
fileName = input("What's the name of the desired file? ")
df = pandas.read_csv(fileName + ".csv")
print(df)

# select which column you wish to delete (working on ability to select multiple)
# if the column has a leading space in front of the column name, it won't recognize
# input that doesn't have it.
# i.e: (Humidity) doesn't work, but ( Humidity) does
# working on making that more intuitive
columnName = input("Which columns would you like to delete? ")
df.drop([columnName], axis=1, inplace = True)
print(df)

# writes a new edited version without selected info (needs work, only writes headers right now)
cf = open(fileName + ".csv")
ef = open(fileName + "_edited.csv", "w")
for line in df:
    ef.write(line)
