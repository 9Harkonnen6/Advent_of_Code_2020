expenses = []
results = []
for c in open("expenses.txt"):
    expenses.append(int(c))

# 1st task, slower coz two loops
for i in expenses:
    for j in expenses:
        if i+j == 2020:
                if i*j not in results:
                    results.append(i*j)
print(results)
results.clear()

# 1st task but different approach (faster) coz only one loop
choosen_number = 0
iterator = 0
while iterator < len(expenses):
    if expenses[choosen_number]+expenses[iterator] == 2020:
        print(f'{expenses[choosen_number]}+{expenses[iterator]}=2020')
        print(expenses[choosen_number]*expenses[iterator])
        break
    else:
        iterator +=1
        if iterator == 200:
            choosen_number +=1
            iterator = 0
        elif iterator == choosen_number:
            iterator +=1
        else:
            pass

choosen_number = 0
choosen_number_2 = 0
iterator = 0

# 2nd task, optimalization is literally non-existing coz of three loops
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i+j+k == 2020:
                if i*j*k not in results:
                    results.append(i*j*k)
print(results)

# 2nd task, optimalised [still working on that]

while iterator < len(expenses):
    if expenses[choosen_number]+expenses[iterator] == 2020:
        print(f'{expenses[choosen_number]}+{expenses[iterator]}=2020')
        print(expenses[choosen_number]*expenses[iterator])
        break
    else:
        iterator +=1
        if iterator == 200:
            choosen_number +=1
            iterator = 0
        elif iterator == choosen_number:
            iterator +=1
        else:
            pass
