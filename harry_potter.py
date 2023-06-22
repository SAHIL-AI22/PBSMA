def sortdates(checkout):
    key = list(map(int, checkout[1].split('-')))
    # print(key)
    key.append(borrowers[checkout[0][0]])
    key.append(checkout[0][1])
    print(tuple(key))
    return tuple(key)


books = dict()
borrowers = dict()
checkouts = dict()
temp = None
while (True):
    line = input()
    if (line == 'Books'):
        temp = 'Books'
        continue
    elif (line == 'Borrowers'):
        temp = 'Borrowers'
        continue
    elif (line == 'Checkouts'):
        temp = 'Checkouts'
        continue
    elif (line == 'EndOfInput'):
        break
    elif (temp == 'Books'):
        access_no, title = line.split('~')
        books[access_no] = title
    elif (temp == 'Borrowers'):
        usercode, name = line.split('~')
        borrowers[usercode] = name
    elif (temp == 'Checkouts'):
        usercode, access_no, due_date = line.split('~')
        checkouts[(usercode, access_no)] = due_date

checkouts = sorted(checkouts.items(), key=sortdates)

for checkout in checkouts:
    line = checkout[1] + '~' + borrowers[checkout[0][0]] + '~' + \
           checkout[0][1] + '~' + books[checkout[0][1]]
    print(line)