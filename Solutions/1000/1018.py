n = int(input())
for _ in range(n):
    ipt = input()
    stack = []
    for x in ipt:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
