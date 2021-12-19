import math


def tokenizer(s):
    res = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = ''
            while s[i].isdigit():
                num += s[i]
                i += 1
            i -= 1
            res.append(int(num))
        elif c in ['[',']',',']:
            res.append(c)
        i += 1
    return res


def old_explode(s):
    # if nested 4 pair -> eplode leftmost pair
    # if num >= 10 -> leftmost regurlar number splits
    s = tokenizer(s)
    left_num_idx = None
    right_num_idx = None
    res = []
    i, nest_cnt = 0, 0
    while i < len(s):
        if s[i] == '[':
            if nest_cnt >= 4:
                n1, n2 = s[i+1], s[i+3]
                print(s[i:i+5])
                if left_num_idx is not None:
                    res[left_num_idx] += n1
                right_num_idx = i + 4
                while right_num_idx < len(s):
                    if isinstance(s[right_num_idx], int):
                        s[right_num_idx] += n2
                        break
                    right_num_idx += 1
                res.append(0)
                nest_cnt -= 1
                i += 4
            else:
                nest_cnt += 1
                res.append(s[i])
        elif s[i] == ']':
            nest_cnt -= 1
            res.append(s[i])
        elif s[i] == ',':
            res.append(s[i])
        elif isinstance(s[i], int):
            left_num_idx = len(res)
            res.append(s[i])
        else:
            raise ValueError
        i += 1
    return ''.join([str(x) for x in res])

def explode(s):
    s = tokenizer(s)
    pair_start_idx = None
    left_num_idx = None
    right_num_idx = None
    stack = []
    i = 0
    while i < len(s):
        if s[i] == ']' and len(stack) > 4:
            pair_end_idx = i
            l, r = s[pair_start_idx+1], s[pair_end_idx-1]
            sub_i = pair_start_idx
            while sub_i >= 0:
                if isinstance(s[sub_i], int):
                    left_num_idx = sub_i
                    break
                sub_i -= 1
            sub_i = pair_end_idx
            while sub_i < len(s):
                if isinstance(s[sub_i], int):
                    right_num_idx = sub_i
                    break
                sub_i += 1
            if left_num_idx is not None:
                s[left_num_idx] += l
            if right_num_idx is not None:
                s[right_num_idx] += r
            ans = s[:pair_start_idx] + [0] + s[pair_end_idx+1:]
            return ''.join([str(x) for x in ans])
        elif s[i] == '[':
            stack.append(s[i])
            pair_start_idx = i
        elif s[i] == ']':
            stack.pop()
        i += 1
    return ''.join([str(x) for x in s])


def split(s):
    s = tokenizer(s)
    res = []
    has_split = False
    for t in s:
        if isinstance(t, int) and t > 9 and not has_split:
            res.append('[')
            res.append(math.floor(t / 2))
            res.append(',')
            res.append(math.ceil(t / 2))
            res.append(']')
            has_split = True
        else:
            res.append(t)
    return ''.join([str(x) for x in res])


def reduce(s):
    while True:
        prev_s = None
        while s != prev_s:
            prev_s = s
            s = explode(s)
        s = split(s)
        if s == prev_s:
            return s
        prev_s = s


def add(s1, s2):
    new_sf = f'[{s1},{s2}]'
    return reduce(new_sf)


def calc_sum(data):
    sum_val = data[0]
    for s in data[1:]:
        sum_val = add(sum_val, s)
    return sum_val


def get_lr(s):
    stack = []
    for i in range(len(s)):
        if s[i] == ',' and len(stack) == 1:
            l = s[1:i]
            r = s[i+1:-1]
            return l, r
        elif s[i] == '[':
            stack.append(s[i])
        elif s[i] == ']':
            stack.pop()


def calc_magnitude(s):
    s = tokenizer(s)
    def recurs(s):
        if len(s) == 1:
            return s[0]
        l, r = get_lr(s)
        return (recurs(l) * 3) + (recurs(r) * 2)
    return recurs(s)

 
with open('input/day_18.txt') as infile:
    data = [x.strip() for x in infile.readlines()]


def part1():
    sum_val = calc_sum(data)
    print(calc_magnitude(sum_val))


def part2():
    from itertools import product
    max_mag = -1
    for s1, s2 in [(s1,s2) for s1,s2 in product(data, data) if s1 != s2]:
        mag = calc_magnitude(add(s1,s2))
        if mag > max_mag:
            max_mag = mag
    print(max_mag)

part1()
part2()


def test_cases():
    print(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]'))

    # explode test case
    test_cases = [
        ('[[[[[9,8],1],2],3],4]','[[[[0,9],2],3],4]'),
        ('[7,[6,[5,[4,[3,2]]]]]','[7,[6,[5,[7,0]]]]'),
        ('[[6,[5,[4,[3,2]]]],1]','[[6,[5,[7,0]]],3]'),
        ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
        ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
    ]
    for s, ans in test_cases:
        assert explode(s) == ans


    # calc mag test cases
    assert calc_magnitude('[[1,2],[[3,4],5]]') == 143
    assert calc_magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]') == 1384
    assert calc_magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]') == 445
    assert calc_magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]') == 791
    assert calc_magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]') == 1137
    assert calc_magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]') == 3488


    assert add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

    test_cases = [
        ('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]','[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]','[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'),
    ]
    for s1, s2, ans in test_cases:
        print(add(s1,s2))
        print(ans)
        assert add(s1,s2) == ans



    data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
    [[[5,[2,8]],4],[5,[[9,9],0]]]
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
    [[[[5,4],[7,7]],8],[[8,3],8]]
    [[9,3],[[9,9],[6,[4,9]]]]
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    data = data.split('\n')

    # print(calc_sum(data))
    assert calc_sum(data) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'


