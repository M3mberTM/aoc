import re
from functools import reduce

def calculate(rows):
    symbol_index = len(rows) -1
    symbols = []
    numbers = []
    for i in range(len(rows)):
        row = rows[i]
        if symbol_index == i:
            matches = re.findall("(\\+|\\*)", row)
            symbols = matches
        else:
            matches = re.findall("\\d+", row)
            numbers.append(matches)
    results = []
    for i in range(len(numbers[0])):
        result = 1
        for row in numbers:
            num = int(row[i])
            if symbols[i] == '*':
                result = result * num
            else:
                result += num
        if symbols[i] == '+':
            result = result - 1
        results.append(result)
    return sum(results)

def row_to_col_num(num_arr):
    i = 0
    numbers = []
    num_string = ""
    while i < len(num_arr[0]):
        num_string = ""
        for num in num_arr:
            if num[len(num)-1-i] != ' ':
                num_string += num[len(num)-1-i]
        if num_string != '':
            numbers.append(int(num_string))
        i += 1
    return numbers


def calculate_updated(rows):
    symbol_index = len(rows) -1
    symbols = []
    numbers = []
    symbols = re.findall("(\\+ +|\\* +)",rows[symbol_index])
    start = 0
    for x in range(len(rows)):
        row = rows[x]
        curr_row = []
        start = 0
        if x < symbol_index:
            for i in range(len(symbols)):
                curr_row.append(row[start:start+len(symbols[i])])
                start = start + len(symbols[i])
            numbers.append(curr_row) 
    result = 0    
    for i in range(len(symbols)):
        column = []
        for x in range(len(numbers)):
            column.append(numbers[x][i])
        nums = row_to_col_num(column)
        if symbols[i].strip() == "*":
            result += reduce(lambda x,y: x*y, nums)
        else:
            result += reduce(lambda x,y: x+y, nums)
    return result

input = None
with open("2025\\inputs\\aoc06.txt") as input_file:
    input = input_file.read()


rows = input.split('\n')
result = calculate_updated(rows)
print(result)
