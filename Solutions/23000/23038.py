n, m = [int(i) for i in input().split()]

box = []
for i in range(3*n) : box.append(list(input()))

for i in range(1, 3*n, 3):
    for j in range(1, 3*m, 3):
        if box[i][j] == "." : box[i][j] = "#"
        if j != 1 and box[i][j-2:j] == ["#", "."] : box[i][j-1] = "#"
        if j != 3*m-2 and box[i][j+1:j+3] == [".", "#"] : box[i][j+1] = "#"
        if i != 1 and box[i-2][j] == "#" and box[i-1][j] == "." : box[i-1][j] = "#"
        if i != 3*n-2 and box[i+1][j] == "." and box[i+2][j] == "#" : box[i+1][j] = "#"

'''        
for i in range(1, 3*n-1):
    for j in range(2, 3*n-2):
        if box[i][j-1 : j+2] == ["#", ".", "#"] : box[i][j] = "#"

for j in range(1, 3*n-1):
    for i in range(2, 3*n-2):
        if box[i][j] == "." and box[i-1][j] == "#" and box[i+1][j] == "#" : box[i][j] = "#"
'''

for line in box: print(''.join(line))

'''
............
.##...###...
.#..........
....#.....#.
....##...##.
....#.....#.
.#.....#....
.##...##....
.#.....#....
..........#.
...###...##.
............

............
.##########.
.#..#.....#.
.#..#.....#.
.#..#######.
.#..#..#..#.
.#..#..#..#.
.#######..#.
.#.....#..#.
.#.....#..#.
.##########.
............
'''