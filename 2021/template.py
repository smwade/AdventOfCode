import os
import sys


# get data path
file_name = os.path.basename(__file__).split('.')[0]
infile = sys.argv[1] if len(sys.argv)>1 else f'input/{file_name}.txt'

with open(infile) as f:
    data = f.readlines()

print(data)
