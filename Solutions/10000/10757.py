# 큰 수 연산 불가능한 경우
a, b = input().split()
c = ""
temp = 0
for i in range(1, max(len(a), len(b)) + 1):
    try:
        s = str(int(a[-i]) + int(b[-i]) + temp)
    except IndexError:
        if len(a) > len(b) : s = str(int(a[-i]) + temp)
        else : s = str(int(b[-i]) + temp)
    if len(s) > 1:
        temp = int(s[0])
        s = s[1]
    else : temp = 0
    c += s
if temp != 0 : c += str(temp)
print(c[::-1])