"""
TODO
The actual net data exceeds 25 GB mem usage before even finishing currently
Eventually hits memory error on my machine (32GB)
Need to cut that down
    -Simplify data structure
    -???
    -less data lmao
"""

import csv

# Specify the filename
filename = 'UHND_Datasets\\netflow_day-21'
dictList = []

# Open the CSV file
with open(filename, mode='r+', newline='') as csvfile:
    #specify field names in order
    #then create DictReader with the csv and fieldnames
    #will format each row as a dictionary using each fieldname as a key
    fieldnames = ["Time","Duration","SrcDevice","DstDevice","Protocol","SrcPort","DstPort","SrcPackets","DstPackets","SrcBytes","DstBytes"]
    csvreader = csv.DictReader(csvfile,fieldnames)
    
    #row_count = sum(1 for row in csvreader) /2
    #print(row_count)
    #iterate over each row
    for row in csvreader:
        #add each row (in dictionary format) to the end of the list
        #if i<row_count:
        dictList.append(row)
        
    #print list for testing
    #print(dictList)
