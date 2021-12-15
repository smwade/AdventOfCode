from collections import Counter, defaultdict


def part_1(state, rules):
    for s in range(10):
        new_state = []
        for i in range(len(state)-1):
            sub_s = state[i:i+2]
            new_state.append(state[i])
            if sub_s in rules:
                new_state.append(rules[sub_s])
        new_state.append(state[-1])
        state = ''.join(new_state)

    c = Counter(state)
    print(max(c.values()) - min(c.values()))


def part_2(state, rules):
    state += '*' # end string token
    state_pairs = [state[i:i+2] for i in range(len(state)-1)]
    state = dict(Counter(state_pairs))

    for _ in range(40):
        new_state = defaultdict(lambda: 0)
        for k, v in state.items():
            if k in rules:
                new_state[k[0] + rules[k]] += v
                new_state[rules[k] + k[1]] += v
            else:
                new_state[k] += v
        state = dict(new_state)

    c_dict = defaultdict(lambda: 0)
    for k, v in state.items():
        c_dict[k[0]] += v

    print(max(c_dict.values()) - min(c_dict.values()))


with open('input/day_14.txt') as f:
    data = [x.strip() for x in f.readlines()]

state, raw_rules = data[0], data[2:]
rules = {}
for rule in raw_rules: 
    k, v = rule.split('->')
    rules[k.strip()] = v.strip()

part_1(state, rules)
part_2(state, rules)

