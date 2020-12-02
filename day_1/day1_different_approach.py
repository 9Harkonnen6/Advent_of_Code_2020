expenses = []
for c in open("expenses.txt"):
    expenses.append(int(c))

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

