import re
import itertools
import numpy as np
from numpy import pi
from math import sin, cos

RANGE = 1000

with open('input/test_19.txt') as infile:
    raw_data = infile.read() 


def parse_data(raw_data):
    raw_data = raw_data.split('\n\n')
    raw_data = [b.split('\n') for b in raw_data]
    data = []
    for beacons in raw_data:
        data.append(np.array([[int(y.strip()) for y in x.split(',')] for x in beacons[1:] if x != '']))
    return data

data = parse_data(raw_data)

# rotation matrix
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

# all rotation matricies
d = [pi/2, pi, (3/2)*pi]
rot_m = []
for t1, t2, t3 in itertools.product(d, d, d):
    r = (Rz(t3) @ Ry(t2) @ Rx(t1)).astype(int)
    rot_m.append(r)


def check_valid(s1, s2):
    for r in rot_m:
        for p1 in s1:
            rot_s2: 
            for p2 in s2:
                pass

