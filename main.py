
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
    allInfo = next(csvreader)
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
            impCases.append(rowCases[i])
    except IndexError:
        impCases.append(rowCases[i - 1])

# This is for only one location
def op1():
    amountCases = 0
    population = 0
    chance = 0
    location = input('enter your location: ')
    loc.append(location)

    for k in citys:
        if (loc[0] == k[3]) or (loc[0] == k[0]):
            loc[0] = k[3]
    for k in citys:
        if (loc[0] == k[3]):
            population = population + int(k[6])
    for j in impCases:
        if loc[0] == j[0]:
            amountCases = int(j[1])

    chance = int(amountCases) / int(population)
    chance = chance * 100
    chance = round(chance, 2)
    print('Your chance of catching covid is about ', chance, ' Percent')


# This is for multiple locations
def op2():
    amountCases = 0
    population = 0
    chance = 0
    boo = True
    count = 0
    final = 0
    while boo:
        count += 1
        print('if you do not have a next stop enter q: ')
        location = input('Where is you #' + str(count) + ' stop: ')
        loc.append(location)
        if location == 'q':
            boo = False


    for i in range(0, len(loc) - 1):
        for k in citys:
            if (i == k[3]) or (i == k[0]):
                i = k[3]
        for k in citys:
            if (i == k[3]):
                population = population + int(k[6])
        for j in impCases:
            if i == j[0]:
                amountCases = int(j[1])

        chance = int(amountCases) / int(population)
        chance = chance * 100

        if i == 0:
            final = chance
        else:
            final = final * chance
        print('Your chance of catching covid is about ', chance, ' Percent')

    chance = round(chance, 2)






loo = True
while loo:
    print('Option 1: You are not traveling')
    print('Option 2: You are going to travel')
    user = int(input('Choose option 1 or 2: '))

    if user == 1:
        op1()
        try:
            user = int(input('press 3 to quit... press anything else to continue'))
        except ValueError:
            loo = True
        try:
            if user == 3:
                loo = False
        except ValueError:
            loo = True
    elif user == 2:
        op2()
        try:
            user = int(input('press 3 to quit... press anything else to continue'))
        except ValueError:
            loo = True
        try:
            if user == 3:
                loo = False
        except ValueError:
            loo = True
    else:
        print('Invalid option input... Try again')
        try:
            user = int(input('press 3 to quit... press anything else to continue'))
        except ValueError:
            loo = True
        try:
            if user == 3:
                loo = False
        except ValueError:
            loo = True