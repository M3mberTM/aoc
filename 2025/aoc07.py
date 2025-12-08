def get_num_of_splits(input):
    manifold = input.split('\n')
    start = manifold[0].index('S')
    splits = 0
    beam_cols = [start]
    beams = [False for i in range(len(manifold[0]))]
    beams[start] = True
    new_beams = []
    for row in manifold:
        while len(beam_cols) > 0:
            beam = beam_cols.pop(0)
            if row[beam] == '^':
                splits += 1
                split_beams = (beam -1, beam+1)
                beams[beam] = False
                for split in split_beams:
                    if split >= 0 and split < len(row):
                        if not beams[split]:
                            new_beams.append(split)
                            beams[split] = True
            else:
                new_beams.append(beam)
        beam_cols = new_beams[:]
        new_beams = []
    return splits

def get_quantum_splits(input):
    manifold = input.split('\n')
    start = manifold[0].index('S')
    splits = 0
    beam_cols = [start]
    beams = [0 for i in range(len(manifold[0]))]
    beams[start] = 1
    new_beams = []
    for row in manifold:
        while len(beam_cols) > 0:
            beam = beam_cols.pop(0)
            if row[beam] == '^':
                split_beams = (beam -1, beam+1)
                for split in split_beams:
                    if split >= 0 and split < len(row):
                        if beams[split] <= 0:
                            new_beams.append(split)
                        beams[split] += beams[beam]
                beams[beam] = 0
            else:
                new_beams.append(beam)
        beam_cols = new_beams[:]
        new_beams = []
    return sum(beams)

        

input = None
with open("2025\\inputs\\aoc07.txt") as input_file:
    input = input_file.read()

splits = get_quantum_splits(input)
print(splits)