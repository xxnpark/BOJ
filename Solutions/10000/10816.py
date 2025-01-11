n = int(input())
table = dict()
for str_num in input().split():
    num = int(str_num)
    if num in table:
        table[num] += 1
    else:
        table[num] = 1
m = int(input())

for str_num in input().split():
    num = int(str_num)
    try:
        print(table[num], end=" ")
    except KeyError:
        print(0, end=" ")
