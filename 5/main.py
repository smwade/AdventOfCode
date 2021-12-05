import re


# read and parse input
with open('input.txt') as f:
    raw_input = f.readlines()
lines = [[int(x) for x in re.findall('\d+', line)] for line in raw_input]

# find bad points
bad_points = {}
bad_cnt = 0
for line in lines:
    line_points = []
    x1, y1, x2, y2 = line
    if x1 == x2:
        x = x1
        for y in range(min(y1,y2), max(y1,y2)+1):
            p = (x,y)
            line_points.append(p)
    elif y1 == y2:
        y = y1
        for x in range(min(x1,x2), max(x1,x2)+1):
            p = (x,y)
            line_points.append(p)
    else:
        pass

    for p in line_points:
        if p not in bad_points:
            bad_points[p] = 1
        else:
            bad_points[p] += 1
            if bad_points[p] == 2:
                bad_cnt += 1

print(bad_cnt)

# part 2
bad_points = {}
bad_cnt = 0
for line in lines:
    line_points = []
    x1, y1, x2, y2 = line
    if x1 == x2:
        x = x1
        for y in range(min(y1,y2), max(y1,y2)+1):
            p = (x,y)
            line_points.append(p)
    elif y1 == y2:
        y = y1
        for x in range(min(x1,x2), max(x1,x2)+1):
            p = (x,y)
            line_points.append(p)
    else:
        if x2 < x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if y2 > y1:
            line_points = zip(range(x1,x2+1), range(y1, y2+1))
        else:
            line_points = zip(range(x1,x2+1), range(y1, y2-1, -1))
        
    for p in line_points:
        if p not in bad_points:
            bad_points[p] = 1
        else:
            bad_points[p] += 1
            if bad_points[p] == 2:
                bad_cnt += 1

print(bad_cnt)
