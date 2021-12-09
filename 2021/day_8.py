
"""
# counts of panels
----------------
# {6: [0, 6, 9], 2: [1], 5: [2, 3, 5], 4: [4], 3: [7], 7: [8]}

# steps
-----------
# learn single ones

# learn a
# 9 has 6 and is diff 4 and a and 1 left
# 0 has 6 has 1 contained
# 6 is remaining with length 6

# 3 is 5 long and has 1 inside
# leaves 2 & 5
### 9 U 2 = 4
### 9 U 5 = 5
"""
import re


with open('input/day_8.txt') as f:
    data = [x.split('|') for x in f.readlines()]
    m = lambda s: re.findall('[\w]+', s)
    data = [[m(l),m(r) ] for l, r in data]



def standardize(s):
    return ''.join(sorted(s))

def diff(s1,s2):
    return standardize(set(s1) - set(s2))

def union(s1,s2):
    return standardize(set(s1) & set(s2))


ans = 0
for row in data:
    left, right = row
    left = [standardize(x) for x in left]
    right = [standardize(x) for x in right]

    m = {}
    for x in left:
        if len(x) == 2: 
            m[x] = 1
            m[1] = x
        if len(x) == 3:
            m[x] = 7
            m[7] = x
        if len(x) == 4:
            m[x] = 4
            m[4] = x
        if len(x) == 7:
            m[x] = 8
            m[8] = x

    for x in [x for x in left if len(x) == 6]:
        if diff(m[4], x) == '':
            m[x] = 9
            m[9] = x
        elif diff(m[1], x) == '' and len(diff(m[4], x)) > 0:
            m[x] = 0
            m[0] = x
        else:
            m[x] = 6
            m[6] = x

    for x in [x for x in left if len(x) == 5]:
        if diff(m[1], x) == '':
            m[x] = 3
            m[3] = x
        elif len(union(m[9], x)) == 4:
            m[x] = 2
            m[2] = x
        elif len(union(m[9], x)) == 5:
            m[x] = 5
            m[5] = x

    row_ans = []
    for x in right:
        row_ans.append(str(m[x]))
    row_ans = int(''.join(row_ans))
    ans += row_ans

print(ans)
