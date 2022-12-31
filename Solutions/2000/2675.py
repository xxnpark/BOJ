for i in range(int(input())):
    lst = input().split()
    print(''.join(list(map(lambda x: x * int(lst[0]), list(lst[1])))))