sum = 0
for s in input():
    if s < "S" : sum += (ord(s) + 1) // 3 - 19
    elif s < "Z" : sum += ord(s) // 3 - 19
    else : sum += 10
print(sum)