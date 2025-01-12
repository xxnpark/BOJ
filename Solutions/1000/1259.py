while (n := input()) != "0":
    while len(n) > 1:
        if n[0] != n[-1]:
            print("no")
            break
        n = n[1:-1]
    else:
        print("yes")
