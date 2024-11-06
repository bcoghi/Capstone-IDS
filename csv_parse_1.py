import csv

# Specify the filename
filename = 'test_net_data.csv'
day02 = 'netflow_day-02/netflow_day-02.csv'
dictList = []

# Open the CSV file
with open(day02, mode='r+', newline='') as csvfile:
    #specify field names in order
    #then create DictReader with the csv and fieldnames
    #will format each row as a dictionary using each fieldname as a key
    fieldnames = ["Time","Duration","SrcDevice","DstDevice","Protocol","SrcPort","DstPort","SrcPackets","DstPackets","SrcBytes","DstBytes"]
    csvreader = csv.DictReader(csvfile,fieldnames)
    
    #iterate over each row 
    for row in csvreader:
        #add each row (in dictionary format) to the end of the list
        dictList.append(row)
        #print(row)
        
    #print list for testing
    #print(dictList)
