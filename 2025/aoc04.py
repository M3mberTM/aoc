def visualize_arr(arr):
    result = ''
    for row in arr:
        result += ''.join(row) + '\n\r'
    print(result)

def get_neighbors(row, col, arr):
    neighbors = [
        [-1, -1],
        [-1,0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1,0],
        [1, 1],
    ]

    arr_neighbors = []

    for neighbor in neighbors:
        vertical = row + neighbor[0]
        horizontal = col + neighbor[1]
        if vertical >= 0 and horizontal >= 0:
            if vertical < len(arr) and horizontal <len(arr[0]):
                try:
                    arr_neighbors.append(arr[vertical][horizontal])
                except:
                    print('Something wrong')
    return arr_neighbors

def is_roll_accessible(row, col,arr):
    roll = '@'
    neighbors = get_neighbors(row, col, arr)
    if neighbors.count(roll) < 4:
        return True
    return False

def get_accessible_rolls(arr):
    roll = '@'
    accessible = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            character = arr[row][col]
            if character == roll:
                if is_roll_accessible(row, col, arr):
                    accessible += 1
    return accessible

def get_accessible_rolls_updated(arr):
    roll = '@'
    accessible = 0
    roll_positions = []
    roll_arr = arr[:]
    for row in range(len(roll_arr)):
        for col in range(len(roll_arr[row])):
            character = roll_arr[row][col]
            if character == roll:
                if is_roll_accessible(row, col, roll_arr):
                    accessible += 1
                    roll_arr[row][col] = '.'
                else:
                    roll_positions.append((row, col))

    new_rolls = []    
    while True:
        for roll in roll_positions:
            if is_roll_accessible(roll[0], roll[1], roll_arr):
                accessible += 1
                roll_arr[roll[0]][roll[1]] = '.'
            else:
                new_rolls.append((roll[0], roll[1]))
        if new_rolls == roll_positions:
            return accessible
        roll_positions = new_rolls[:]
        new_rolls = []
        # visualize_arr(roll_arr)
        # print('----------\n')

input = None
with open("2025\\inputs\\aoc04.txt") as input_file:
    input = input_file.read()

rows = input.split('\n')
arr = []
for row in rows:
    arr.append(list(row))

rolls = get_accessible_rolls_updated(arr)
print(rolls)