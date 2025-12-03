def get_joltage(value):
    best_first_val = 0
    first_index = -1
    for i in range(len(value)-1):
        curr_val = int(value[i])
        if best_first_val < curr_val:
            best_first_val = curr_val
            first_index = i
    best_second_val = 0
    for i in range(len(value)-1-first_index):
        curr_val = int(value[first_index+i+1])
        if best_second_val < curr_val:
            best_second_val = curr_val
    return int(str(best_first_val)+str(best_second_val))

def get_joltage_updated(bank, battery_count):
    battery = ''
    best_index = 0
    curr_top = 0
    i = 0
    # can only get the top value until the final x digits, where x represents the amount of digits still required to put into the battery
    while len(battery) < 12:
        curr_val = int(bank[i])
        if curr_top < curr_val:
            curr_top = curr_val
            best_index = i
        if i >= len(bank) - battery_count + len(battery):
            i = best_index
            battery += bank[best_index]
            curr_top = 0
        i += 1
    return int(battery)

input = None
with open("2025\\inputs\\aoc03.txt") as input_file:
    input = input_file.read()

input_vals = input.split('\n')

total = 0
for val in input_vals:
    joltage = get_joltage_updated(val, 12)
    # print(joltage)
    total += joltage

print(total)