
# Cruzhacks 2021
# covid approximation meter

import csv

city = "uscities.csv"
cases = "county_cases.csv"

allInfo = []
casesInfo = []
rowCases = []

# This one has all the City data
citys = []
# This one has all the data for cases
impCases = []
# Location of the user
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

# This is importing all the individual county cases to impCases
for i in range(0, len(rowCases)):
    try:
        if rowCases[i+1][0] != rowCases[i][0]:
            impCases.append(rowCases[i])
    except IndexError:
        impCases.append(len(rowCases) - 1)

# This is for only one location
def op1():
    amountCases = 0
    population = 0
    chance = 0
    location = input('enter your location: ')
    loc.append(location)

    for i in citys:
        if loc[0] is i[3]:
            population = i[6]
    for i in impCases:
        if loc[0] is i[0]:
            cases = i[1]

    chance = amountCases/population
    print('Your chance of catching covid is about ', chance, ' Percent')

# This is for multiple locations
def op2():
    boo = True
    count = 0
    while boo:
        count += 1
        print('if you do not have a next stop enter q')
        location = input('Where is you #' + str(count) + ' stop')
        loc.append(location)
        if location == 'q':
            boo = False


loo = True
while loo:
    print('Option 1: You are not traveling')
    print('Option 2: You are going to travel')
    user = int(input('Choose option 1 or 2: '))

    if user == 1:
        op1()
        user = int(input('press 3 to quit... press anything else to continue'))
        if user == 3:
            loo = False
    elif user == 2:
        op2()
        user = int(input('press 3 to quit... press anything else to continue'))
        if user == 3:
            loo = False
    else:
        print('Invalid option input... Try again')
        user = int(input('press 3 to quit... press anything else to continue'))
        if user == 3:
            loo = False
