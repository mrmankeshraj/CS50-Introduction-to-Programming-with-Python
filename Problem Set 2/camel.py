line = input()

for i in line:
    if i.isupper():
        line = line.replace(i, "_" + i.lower())
    
print(line)