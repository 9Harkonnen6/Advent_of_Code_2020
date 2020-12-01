expenses = []
for c in open("day_1/expenses.txt"):
    expenses.append(int(c))

for i in expenses:
    for j in expenses:
        if i+j == 2020:
            print(i*j)
