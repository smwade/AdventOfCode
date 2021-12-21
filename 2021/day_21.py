import re


with open('input/day_21.txt') as infile:
    raw_data = infile.read()
raw_data = re.findall(r'\d', raw_data)
p1_start, p2_start = [int(x) for x in [raw_data[1], raw_data[3]]]


def roll_gen():
    die_state = 1
    while True:
        if die_state > 100:
            die_state = 1
        yield die_state
        die_state += 1


def get_state(cur_state, turn_roll):
    val = ((cur_state + turn_roll) % 10)
    if val == 0:
        val = 10
    return val


def part1(p1_state, p2_state):
    p1_score, p2_score = 0, 0
    roll = roll_gen()
    roll_cnt = 0
    while True:
        turn_roll = sum([next(roll) for _ in range(3)])
        roll_cnt += 3
        p1_state = get_state(p1_state, turn_roll)
        p1_score += p1_state
        if p1_score >= 1000:
            break
        turn_roll = sum([next(roll) for _ in range(3)])
        roll_cnt += 3
        p2_state = get_state(p2_state, turn_roll)
        p2_score += p2_state
        if p2_score >= 1000:
            break
    
    return min(p1_score, p2_score) * roll_cnt


def part2(p1_state, p2_state):
    d_map = {
        3 : 1,
        4 : 3,
        5 : 6,
        6 : 7,
        7 : 6,
        8 : 3,
        9 : 1,
    }
    memo = {}
    def recurse(p1_state, p2_state, p1_score, p2_score, p1_turn):
        s = (p1_state, p2_state, p1_score, p2_score, p1_turn)
        if s in memo:
            return memo[s]
        if p1_score >= 21:
            return 1, 1
        if p2_score >= 21:
            return 0, 1
        p1_win_list = []
        game_cnt_list = []
        for r in range(3,10):
            _p1_state, _p2_state, _p1_score, _p2_score, _p1_turn = p1_state, p2_state, p1_score, p2_score, p1_turn
            if _p1_turn:
                _p1_state = get_state(_p1_state, r)
                _p1_score += _p1_state
            else:
                _p2_state = get_state(_p2_state, r)
                _p2_score += _p2_state
            _p1_turn = not _p1_turn
            p1_win, total_games = recurse(_p1_state, _p2_state, _p1_score, _p2_score, _p1_turn)
            p1_win_list.append(p1_win * d_map[r])
            game_cnt_list.append(total_games * d_map[r])
        ans = sum(p1_win_list), sum(game_cnt_list)
        memo[s] = ans
        return ans

    p1_win, game_cnt = recurse(p1_state, p2_state, 0, 0, True) 
    return max(p1_win, game_cnt-p1_win), p1_win, game_cnt-p1_win, game_cnt


"""
def num_ways(val, num_dice, num_sides=3):
    if num_dice == 1 and 1 <= val <= num_sides:
        return 1
    if num_dice == 1 and not (1 <= val <= num_sides):
        return 0
    num_way_list = []
    for r in range(1, num_sides+1):
        num_way_list.append(num_ways(val-r, num_dice-1, num_sides))
    return sum(num_way_list) 

num_sides = 3
num_dice = 3
for i in range(num_dice, (num_dice * num_sides)+1):
    print(f'{i}: {num_ways(i, num_dice, num_sides)}')
"""


print(part2(p1_start, p2_start))
