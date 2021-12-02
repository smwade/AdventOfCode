# part 1
with open('input.txt') as f:
    data = [x.rsplit() for x in f.readlines()]

h_pos, v_pos = 0, 0
for direction, val in data:
    val = int(val)
    if direction == 'forward':
        h_pos += val
    if direction == 'down':
        v_pos += val
    if direction == 'up':
        v_pos -= val

print(h_pos * v_pos)
    

# part 2
h_pos, v_pos, aim = 0, 0, 0
for direction, val in data:
    val = int(val)
    if direction == 'forward':
        h_pos += val
        v_pos += aim * val
    if direction == 'down':
        aim += val
    if direction == 'up':
        aim -= val

print(h_pos * v_pos)
    
