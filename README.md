
# PART 1 - Scenario
Our problems revolve around correlating data sets and producing resulting data sets
efficiently. The following problem is to merge two data sets according to specific
rules as specified in the task. Once the data sets have been merged answer the
following questions:
- What is the location of the user at 12:00 on 24 September 2021 GMT?
- What is the location of the user at 14:10 on 24 September 2021 GMT?
You are given two files:
- City list containing a list of cities and their HASH value
- List of locations and Unix timestamps
- Both files are CSV - Comma separated files

# Task
1. Create a python script that processes both CSV files
2. Correlate the HASH values in target.csv file with the HASH values from the City
list lookup CSV file
3. Using python code, identify the last known location before 12:00 and 14:10 and
print out both locations on a separate line
4. Write a short description of how your code works
5. Use python3