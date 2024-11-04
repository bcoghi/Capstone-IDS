import csv

# Specify the filename
filename = 'test_net_data.csv'
data_list = []
# Open the CSV file
with open(filename, mode='r+', newline='') as csvfile:
    # Create a CSV reader
    csvreader = csv.DictReader(csvfile)
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(["Time","Duration","SrcDevice","DstDevice","DstPackets","SrcBytes","DstBytes"])
    csvwriter.writerow(["Time","Duration","SrcDevice","DstDevice","DstPackets","SrcBytes","DstBytes"])
    # Get the header (first row)
    #header = next(csvreader)
    #print(f'Header: {header}')
    
    # Read the remaining rows
    for row in csvreader:
        print(row)
        data_list = [row for row in csvreader]

    print(data_list)
