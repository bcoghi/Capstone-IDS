import csv

# Specify the filename
filename = 'C:\\Users\\bcoghi\\Downloads\\netflow_day-02\\data.csv'

# Open the CSV file
with open(filename, mode='r', newline='') as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile)
    
    # Get the header (first row)
    #header = next(csvreader)
    #print(f'Header: {header}')
    
    # Read the remaining rows
    for row in csvreader:
        print(row)
