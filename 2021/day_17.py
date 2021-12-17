import re
import math

# target area: x=124..174, y=-123..-86

def read_input():
    with open('input/day_17.txt') as infile:
        data = infile.readline()
    return data


def parse_input(data):
    data = re.findall(r'(-?\d+)..(-?\d+)', data)
    x_window = [int(x) for x in data[0]]
    y_window = [int(x) for x in data[1]]
    return x_window, y_window


get_y_pos = lambda v, t: (v*t) - (t*(t-1)/2) 
get_x_pos = lambda v, t: get_y_pos(v,t) if t <= v else get_y_pos(v,v)


x_window, y_window = parse_input(read_input())

# get range of min and max velocity
yv_min = y_window[0]
yv_max = (-1 * y_window[0]) - 1
xv_max = x_window[1]
for xv in range(1, xv_max):
    if get_x_pos(xv, xv) >= x_window[0]:
        xv_min = xv
        break


# part 1
# best hit point is at (xv_min, yv_max)
print(get_y_pos(yv_max, yv_max))


# part 2
hit_counts = 0
for xv in range(xv_min, xv_max+1):
    for yv in range(yv_min, yv_max+1):
        t = 0
        x, y = 0, 0
        while x <= x_window[1] and y >= y_window[0]:
            t += 1
            x = get_x_pos(xv, t)
            y = get_y_pos(yv, t)
            if x_window[0] <= x <= x_window[1] and y_window[0] <= y <= y_window[1]:
                hit_counts += 1
                break
print(hit_counts)

