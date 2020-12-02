data = []
results = []
for c in open("day_2/passwords.txt"):
    data.append(c)

# 1st task
for e in data:
    # extracted times the letter can ocurr
    x = int(e[0:e.index('-')])
    y = int(e[(e.index('-')+1):e.index(' ')])
    letter = e[e.index(' ')+1]
    password = e[e.index(':')+2:-1]
    
    # logic
    if list(password).count(letter) in range(x,y+1):
        results.append(password)
        
print(len(results))
results.clear()
# 2nd task
for e in data:
    x = int(e[0:e.index('-')])
    y = int(e[(e.index('-')+1):e.index(' ')])
    letter = e[e.index(' ')+1]
    password = e[e.index(':')+2:-1]

    # logic
    if  password[x-1] == letter and password[y-1] == letter:
        pass
    elif password[x-1] != letter and password[y-1] != letter:
        pass
    else:
        results.append(e)
print(len(results))