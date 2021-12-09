import os
import sys


# get data path
file_name = os.path.basename(__file__).split('.')[0]
infile = sys.argv[1] if len(sys.argv)>1 else f'input/{file_name}.txt'

with open(infile) as f:
    data = [x.strip() for x in f.readlines()]
    data = [[int(x) for x in row] for row in data]


def get_neighbors(arr, row, col):
    neighbors = []
    if row-1 >= 0: neighbors.append((row-1,col))
    if row+1 < len(arr): neighbors.append((row+1,col))
    if col-1 >= 0: neighbors.append((row,col-1))
    if col+1 < len(arr[row]): neighbors.append((row,col+1))
    return neighbors

lps = []
for row in range(len(data)):
    for col in range(len(data[row])):
        val = data[row][col]
        is_low = True
        for (n_row, n_col) in get_neighbors(data,row,col):
            if val >= data[n_row][n_col]:
                is_low = False
        if is_low:
            lps.append((row,col))

# part 1
print(sum([data[row][col]+1 for row, col in lps]))


# part 2
basin_cnts = []
for p in lps:
    s = set(p)
    stack = [p]
    cnt = 0
    while len(stack) > 0:
        p = stack.pop()
        cnt += 1
        good_neighbors = []
        for n in get_neighbors(data,p[0],p[1]):
            if n in s:
                continue
            if data[n[0]][n[1]] < data[p[0]][p[1]]:
                continue
            if data[n[0]][n[1]] == 9:
                continue
            good_neighbors.append(n)
        s.update(good_neighbors)
        stack += good_neighbors 

    basin_cnts.append(cnt)

ans = sorted(basin_cnts, reverse=True) 
print(ans)
print(ans[0] * ans[1] * ans[2])








