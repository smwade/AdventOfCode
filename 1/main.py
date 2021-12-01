# load input data
with open('./input.txt') as f:
    data = [int(x) for x in f.readlines()]


# Part 1
def get_increase_count(s):
    count = 0
    for x, y in zip(s, s[1:]):
        if y > x:
            count += 1
    return count

print('Part 1:')
res = get_increase_count(data)
print(res)


# Part 2
def window_series(s, window_size=3):
    new_s = []
    for i in range(len(s)):
        start = i
        end = i+window_size
        if end <= len(s):
            window = s[start:end]
            new_s.append(sum(window))
    return new_s

print('Part 2:')
window_data = window_series(data)
res = get_increase_count(window_data)
print(res)

