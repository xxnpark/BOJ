n = int(input())
five = n // 5
cases = []
while five >= 0:
    three = (n - five * 5) / 3
    if float(int(three)) == three : cases.append(int(three) + five)
    five -= 1
if cases : print(min(cases))
else : print(-1)