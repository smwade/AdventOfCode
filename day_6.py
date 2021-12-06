with open('input/day_6.txt') as f:
    data = [int(x) for x in f.readline().split(',')]


# part 1
def part_1(data):
    state = data
    n_days = 80
    for day in range(n_days):
        new_state = []
        for fish in state:
            if fish == 0:
                new_state.append(6)
                new_state.append(8)
            else:
                fish -= 1
                new_state.append(fish)
        state = new_state

    print(len(state))


# part 2
from collections import Counter

def add_fish(state, fish_state, num_fish):
    if fish_state not in state:
        state[fish_state] = 0
    state[fish_state] += num_fish
    return state

state = dict(Counter(data))
n_days = 256

for day in range(n_days):
    new_state = {}
    for fish_state, num_fish in state.items():
        if fish_state == 0:
            new_state = add_fish(new_state, 6, num_fish)
            new_state = add_fish(new_state, 8, num_fish)
        else:
            new_state = add_fish(new_state, fish_state-1, num_fish)
    state = new_state

print(sum(state.values()))
