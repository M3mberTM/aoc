start_val = 50
min_val = 0
max_val = 99

def rotate_dial(start: int, dir: str, amount: int)->int:
    if dir == 'R':
        # rotate right
        remainder = amount % (max_val + 1)
        new_val = start + remainder
        if new_val > max_val:
            new_val = new_val - max_val + min_val -1
        return new_val
    else: 
        # rotate left
        remainder = amount % (max_val + 1)
        new_val = start - remainder
        if new_val < min_val:
            new_val = max_val - abs(new_val) + 1
        return new_val

def rotate_dial_updated(start: int, dir: str, amount: int)->tuple[int,int]:
    count = 0
    if dir == 'R':
        # rotate right
        count = count + (amount // (max_val + 1))
        remainder = amount % (max_val + 1)
        new_val = start + remainder
        if new_val > max_val:
            new_val = new_val - max_val + min_val -1
            count = count + 1
        return new_val, count
    else: 
        # rotate left
        count = count + (amount // (max_val + 1))
        remainder = amount % (max_val + 1)
        new_val = start - remainder
        if new_val < min_val:
            new_val = max_val - abs(new_val) + 1
            if start != 0:
                count = count + 1
        if new_val == 0:
            count = count + 1
        return new_val, count

input = None
with open("inputs\\aoc01.txt") as input_file:
    input = input_file.read()

input_vals = input.split('\n')
curr_dial = start_val
zero_count = 0
for i in range(len(input_vals)):
    val = input_vals[i]
    dir = val[0]
    amount = int(val[1:])
    curr_dial, dial_count = rotate_dial_updated(curr_dial, dir, amount)
    print(curr_dial)
    zero_count = zero_count + dial_count

print('Password is: ', zero_count)