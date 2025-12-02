import re
def is_id_invalid(id):
    string_id = str(id)
    return string_id[0:len(string_id)//2] == string_id[len(string_id)//2:]

def is_id_invalid_updated(id):
    string_id = str(id)
    result = re.search("^(\\d+)\\1+$", string_id)
    return result != None

def get_invalid_id_total(start, stop):
    curr_total = 0
    for i in range(stop - start + 1):
        if is_id_invalid_updated(start + i):
            curr_total += start + i
    return curr_total


input = None
with open("2025\\inputs\\aoc02.txt") as input_file:
    input = input_file.read()

input_vals = input.split(",")
total = 0
for val in input_vals:
    curr_val = val.strip()
    id_start = int(curr_val[0:curr_val.index('-')])
    id_end = int(curr_val[curr_val.index('-')+1:])
    total += get_invalid_id_total(id_start, id_end) 

print(total)
