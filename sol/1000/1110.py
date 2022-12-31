i = 0
ipt = input()
num = ipt
while True:
    if len(num) == 1: num = "0" + num
    num = str(num[1] + str(int(num[0]) + int(num[1]))[-1])
    i += 1
    if int(num) == int(ipt):
        print(i)
        break