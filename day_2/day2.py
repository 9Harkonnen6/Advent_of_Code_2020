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