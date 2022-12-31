str = input().upper()
alp = []
count = []
for x in set(str):
    alp.append(x)
    count.append(str.count(x))
if count.count(max(count)) == 1:
    print(alp[count.index(max(count))])
else : print("?")