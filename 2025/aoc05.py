def get_num_of_fresh(ranges, ids):
    correct = 0
    range_tuples = []
    for range in ranges:
        vals = range.split('-')
        range_tuples.append((int(vals[0]), int(vals[1])))
    for id in ids:
        id_num = int(id)
        for range in range_tuples:
            if id_num >= range[0] and id_num <= range[1]:
                correct += 1
                break
    return correct

def get_fresh_val_count(ranges):
    fresh_ids = [] 
    sorted_ranges = []
    bounds = []
    for value in ranges:
        vals = value.split('-')
        lower_bound = int(vals[0])
        upper_bound = int(vals[1])
        sorted_ranges.append((lower_bound, upper_bound))
    sorted_ranges.sort(key=lambda val: val[0])
    found_bound = False
    for value in sorted_ranges:
        lower_bound = value[0]
        upper_bound = value[1]
        found_bound = False
        for bound in bounds:
            if lower_bound <= bound[1]:
                if upper_bound > bound[1]:
                    bound[1] = upper_bound
                found_bound = True
        if not found_bound:
            bounds.append([lower_bound, upper_bound])
    
    correct = 0
    for bound in bounds:
        correct += bound[1] - bound[0] + 1
    return correct


input = None
with open("2025\\inputs\\aoc05.txt") as input_file:
    input = input_file.read()

rows = input.split('\n')
ranges = []
ids = []
for i in range(len(rows)):
    if len(rows[i]) < 1:
        ids = rows[i+1:]
        break
    else:
        ranges.append(rows[i])

correct = get_fresh_val_count(ranges)
print(correct)