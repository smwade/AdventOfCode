import re
import itertools
import numpy as np
from numpy import pi
from math import sin, cos
from collections import defaultdict


with open('input/day_19.txt') as infile:
    raw_data = infile.read() 


# get all rotation matricies
Rx = lambda x: np.array([
    [1, 0, 0],
    [0, cos(x), -sin(x)],
    [0, sin(x), cos(x)],
])
Ry = lambda x: np.array([
    [cos(x), 0, sin(x)],
    [0, 1, 0],
    [-sin(x), 0, cos(x)],
])
Rz = lambda x: np.array([
    [cos(x), -sin(x), 0],
    [sin(x), cos(x), 0],
    [0, 0, 1],
])

d = [0, pi/2, pi, (3/2)*pi]
rot_m = []
for t1, t2, t3 in itertools.product(d, d, d):
    r = (Rz(t3) @ Ry(t2) @ Rx(t1)).astype(int)
    rot_m.append(r)

s = set()
rotations = []
for r in rot_m:
    k = ''.join([str(x) for x in r.flatten()])
    if k not in s:
        s.add(k)
        rotations.append(r)


def parse_data(raw_data):
    raw_data = raw_data.split('\n\n')
    raw_data = [b.split('\n') for b in raw_data]
    data = []
    for beacons in raw_data:
        data.append(np.array([[int(y.strip()) for y in x.split(',')] for x in beacons[1:] if x != '']))
    return data
data = parse_data(raw_data)

def transform_ref(s1, s2):
    for r in rotations:
        s2_hat = s2 @ r
        d = defaultdict(lambda: 0)
        for p1 in s1:
            for p2 in s2_hat:
                offset = p1 - p2
                key = (offset[0], offset[1], offset[2])
                d[key] += 1
                if d[key] >= 12:
                    return s2_hat + offset, offset
    return None


def match(matched, unmatched, sensor_locs):
    for i, um in enumerate(unmatched):
        for base in matched:
            res = transform_ref(base, um)
            if res is not None:
                norm_um, s = res
                sensor_locs.append(s)
                unmatched.pop(i)
                matched.append(norm_um)
                return matched, unmatched, sensor_locs


unmatched = data[1:]
matched = [data[0]]
sensor_locs = [np.array([0,0,0])]
while len(matched) < len(data):
    matched, unmatched, sensor_locs = match(matched, unmatched, sensor_locs)

all_beacons = set()
for s in matched:
    for b in s:
        all_beacons.add((b[0], b[1], b[2]))
print('Part 1:')
print(len(all_beacons))

max_dist = 0
for s1 in sensor_locs:
    for s2 in sensor_locs:
        dist = np.sum(np.abs(s2 - s1))
        if dist > max_dist:
            max_dist = dist
print('Part 2:')
print(max_dist)


