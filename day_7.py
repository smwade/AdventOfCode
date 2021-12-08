with open('input/day_7.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

# part 1
data = sorted(data)
m = len(data) // 2
dist_func = lambda x: abs(x - data[m])
ans = sum([dist_func(x) for x in data])
print(ans)

# part 2
m = sum(data) // len(data)
dist_list = []
for c in range(m-2,m+2):
    dist_func = lambda x, c: abs(x-c)*(abs(x-c)+1)/2 
    dist_list.append(sum([dist_func(x, c) for x in data]))
print(max(dist_list))
