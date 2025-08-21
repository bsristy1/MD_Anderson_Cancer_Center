with open('table2.csv', 'r') as f:
    c = 0
    lines = f.readlines()
    for line in lines:
        if line.startswith('sp') or line.startswith('tr'):
            c +=1


print(c)