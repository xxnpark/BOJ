for i in range(int(input())):
    h, w, n = map(int, input().split())
    if str(n % h) == "0":
        x = str(n // h)
        y = str(h)
    else:
        x = str(n // h + 1)
        y = str(n % h)
    if len(x) == 1 : x = "0" + x
    print(y + x)