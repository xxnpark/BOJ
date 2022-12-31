def inplanet(x, y, r, a, b) :
    if ((x-a)**2 + (y-b)**2)**(1/2) <= r : return True
    else : return False

cases = int(input())

for i in range(cases) :
    x1, y1, x2, y2 = [int(n) for n in input().split()]
    planets = int(input())
    num = 0
    for j in range(planets) :
        x, y, r = [int(n) for n in input().split()]
        if inplanet(x, y, r, x1, y1) != inplanet(x, y, r, x2, y2) :
            num += 1
    print(num)