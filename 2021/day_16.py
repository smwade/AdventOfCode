from dataclasses import dataclass
import math


@dataclass
class Packet:
    version: str
    type_id: str
    start_idx: int
    end_idx: int


@dataclass
class ValuePacket(Packet):
    value: int


@dataclass
class OperatorPacket(Packet):
    len_type_id: int
    sub_packets: list[Packet]


def read_input():
    with open('input/day_16.txt') as infile:
        data = infile.readline()
    return data


def hex_2_bin(hex_str):
    HEX_MAP = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    res = ''
    for c in hex_str:
        res += HEX_MAP[c]
    return res

version_sum = 0

def parse_packet(s, cur):

    # parse version and type
    start_cur = cur
    version = int(s[cur:cur+3], 2)
    type_id = int(s[cur+3:cur+6], 2)
    cur += 6

    if type_id == 4:
        packet_val_peices = []
        flag = None
        while flag != '0':
            flag = s[cur]
            sub_s = s[cur+1:cur+5]
            cur += 5
            packet_val_peices.append(sub_s)
        value = int(''.join(packet_val_peices), 2)
        return ValuePacket(
                version=version,
                type_id=type_id,
                value=value,
                start_idx=start_cur,
                end_idx=cur
            )
    else:
        sub_packets = []
        len_type_id = s[cur]
        cur += 1
        if len_type_id == '0':
            num_bytes = int(s[cur:cur+15], 2)
            cur += 15

            used_bytes = 0
            while used_bytes < num_bytes:
                packet = parse_packet(s, cur)
                used_bytes += packet.end_idx - packet.start_idx
                cur = packet.end_idx
                sub_packets.append(packet)

        else:
            num_sub_packets = int(s[cur:cur+11], 2)
            cur += 11

            while len(sub_packets) < num_sub_packets:
                packet = parse_packet(s, cur)
                cur = packet.end_idx
                sub_packets.append(packet)

        return OperatorPacket(
                version=version,
                type_id=type_id,
                start_idx=start_cur,
                end_idx=cur,
                len_type_id=len_type_id,
                sub_packets=sub_packets
            ) 


def parse_data(input_data):
    min_packet_size = 12
    bin_data = hex_2_bin(input_data)
    cur = 0
    packet_list = []
    while cur < len(bin_data) - 12:
        packet = parse_packet(bin_data, 0)
        cur += packet.end_idx
        packet_list.append(packet)
    return packet_list


# part 1
res = parse_data(read_input())
stack = res
version_sum = 0
while stack:
    packet = stack.pop()
    if isinstance(packet, OperatorPacket):
        version_sum += packet.version
        stack += packet.sub_packets
    else:
        version_sum += packet.version
print(version_sum)


# part 2
operation_map = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0, 
}

def eval_expr(p):
    if isinstance(p, ValuePacket):
        return p.value
    return operation_map[p.type_id]([eval_expr(x) for x in p.sub_packets])

res = parse_data(read_input())
print(eval_expr(res[0]))

