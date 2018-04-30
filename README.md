# remove-pii
Script for assisting in the easy removal of PII from .CSV files

*Only works with .csv at this time*

Instructions

1. Place in the directory with files you want to clean

2. Run in terminal with command "python no-pii.py"

3. When prompted, type in the name of the desired file (don't include extension)

4. A bit of sample data from your file will print to the console

5. The script will do a search of column headers to look for likely PII

6. List of possible PII headers will print to console

7. If the search found all the columns you want deleted, answer next question with "no", script will delete those columns and ask if you are finished

8. If the search missed columns you want deleted, then answer 'yes'

9. When prompted, input name of column you want deleted

10. If you need to add multiple columns, repeat steps 8 & 9 as necessary

11. Once you have added all the columns you need, answer 'no' and run the deletion

12. If finished, answer the final question with 'yes'

13. Voila! You now have a clean file!
