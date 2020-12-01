expenses = []
for c in open(f"expenses.txt"):
    expenses.append(int(c))

for i in expenses:
    for j in expenses:
        if i+j == 2020:
            print(f'{i} + {j} = 2020')