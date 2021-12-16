from heapq import heappush, heappop


with open('input/day_15.txt') as infile:
    data = infile.readlines()
    data = [[int(x) for x in y.strip()] for y in data]


def part_1(data):
    m, n = len(data), len(data[0])
    heap = []
    s = set()
    cost = [[None for _ in range(n)] for _ in range(m)]
    start = (0,0)
    heappush(heap, (0, start))
    s.add(start)
    while heap:
        val, cur_pos = heappop(heap)
        s.remove(cur_pos)
        row, col = cur_pos
        cost[row][col] = val # check
        if cur_pos == (m-1,n-1): return val

        # get neighbors
        neighbors  = []
        if row < m-1: neighbors.append((row+1,col))
        if row > 0: neighbors.append((row+-1,col))
        if col < n-1: neighbors.append((row,col+1))
        if col > 0: neighbors.append((row,col-1))

        for neighbor in neighbors:
            nr, nc = neighbor
            step_val = val + data[nr][nc]
            if cost[nr][nc] is None or cost[nr][nc] > step_val:
                if neighbor not in s:
                    heappush(heap, (step_val, neighbor))
                    s.add(neighbor)


def generate_full_data(data):
    def calc_val(x):
        if x == 9:
            return 9
        return x % 9

    M = []
    for ri in range(5):
        for row in data:
            full_row = []
            for ci in range(5):
                for v in row:
                    full_row.append(calc_val(v + ci + ri))
            M.append(full_row)
    return M


def part_2(data):
    full_data = generate_full_data(data)
    print(part_1(full_data))


print(part_1(data))
print(part_2(data))

