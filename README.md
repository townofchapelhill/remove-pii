# remove-pii
Script for assisting in the easy removal of PII from .CSV files

*Only works with .csv at this time*

Instructions

1. Place in the directory with files you want to clean

2. Run in terminal with python no-pii.py

3. When prompted, type in the name of the desired file (don't include extension)

4. A bit of sample data from your file will print to the console

5. On next prompt, input which column name you want to clean

*Can currently only handle one column at a time*

6. If you have more columns you wish to clean, answer next question with 'yes'

7. If yes, repeat steps 1-6

8. If no, the new file will write in the same directory

9. Voila! You now have a clean file! (Sort of, I've still got bugs to work out)
