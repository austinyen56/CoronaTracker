
# csv file tester

import csv

city = "uscities.csv"
cases = "county_cases.csv"

allInfo = []

# This one has all the City data
citys = []

casesInfo = []
rowCases = []

impCases = []

loc = []

with open(city, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
         citys.append(row)

with open(cases, 'r') as csvfileInfo:
    csvreader = csv.reader(csvfileInfo)
    casesInfo = next(csvreader)
    for row in csvreader:
        rowCases.append(row)


for i in range(0, len(rowCases)):
    try:
        if rowCases[i+1][0] != rowCases[i][0]:
            #print(rowCases[i][0])
            impCases.append(rowCases[i])
    except IndexError:
        #print(rowCases[len(rowCases) - 1][0])
        impCases.append(rowCases[i - 1])


#print(impCases)
#thing = 'Yolo'
#for i in range(0, len(impCases) - 1):
#    try:
#        print(impCases[i].index(thing))
#    except:
#        print('not in this index')
#

#for i in citys:
#    print(i[6])

amountCases = 0
population = 0
chance = 0
location = input('enter your location: ')
loc.append(location)

for i in citys:
    if loc[0] == i[3]:
        population = i[6]

for i in impCases:
    if loc[0] == i[0]:
        amountCases = int(i[1])

print(int(amountCases), int(population))
chance = int(amountCases) // int(population)
print('Your chance of catching covid is about ', chance, ' Percent')

