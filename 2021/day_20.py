import numpy as np


with open('input/day_20.txt') as infile:
    data = [x.strip() for x in infile.readlines()]

enhance_algo = data[0]
input_img = [[y for y in x] for x in data[2:]]


def pad(M, pad=1, pad_val='.'):
    m, n = len(M), len(M[0])
    res = [[pad_val for _ in range(m + (pad * 2))] for _ in range(pad)]
    for row in M:
        res.append([pad_val]*pad + row + [pad_val]*pad)

    res = res + [[pad_val for _ in range(m + (pad * 2))] for _ in range(pad)]
    return res

def display(M):
    pass
    #print(np.array(M))


def get_bright_pix(num_enhance):

    M = pad(input_img, pad=5)
    display(M)
    for i in range(num_enhance):
        M_new = []
        for row in range(1,len(M)-1):
            new_row = []
            for col in range(1,len(M[0])-1):
                conv_res = []
                for i in range(-1,2,1):
                    for v in M[row+i][col-1:col+2]:
                        b_val = 1 if v == '#' else 0
                        conv_res.append(b_val)
                conv_num = int(''.join([str(x) for x in conv_res]),2)
                new_row.append(enhance_algo[conv_num])
            M_new.append(new_row)
        M = pad(M_new, pad=2, pad_val=M_new[0][0])

    cnt = 0
    for row in M:
        for val in row:
            if val == '#':
                cnt += 1
    return cnt

# part 1
print(get_bright_pix(2))

# part 2
print(get_bright_pix(50))

