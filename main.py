
# Cruzhacks 2021
# covid approximation meter


loc = []


def op1():
    location = input('enter your location')


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
