expenses = []
results = []
for c in open("day_1/expenses.txt"):
    expenses.append(int(c))

# 1st task
for i in expenses:
    for j in expenses:
        if i+j == 2020:
                if i*j not in results:
                    results.append(i*j)
print(results)
results.clear()
# 2nd task
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i+j+k == 2020:
                if i*j*k not in results:
                    results.append(i*j*k)
print(results)
