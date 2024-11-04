import json

filename = 'host_test_data.json'
dictList = []

with open(filename, 'r') as input:
    for line in input:
        row = json.loads(line)
        dictList.append(row)

"""
c = 0
for row in dictList:
    print(dictList[c])
    c = c + 1
"""
print(dictList)    
