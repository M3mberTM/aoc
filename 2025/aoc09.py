import matplotlib.pyplot as plt

class Aoc:
    def __init__(self, input):
        coords = []
        for line in input:
            x,y = list(map(int, line.split(",")))
            coords.append((x,y))
        self.input = coords
    
    def part_one(self):
        coords = self.input[:]
        top_area = 0
        for i in range(len(coords)):
            for x in range(len(coords)):
                if x > i:
                    area = abs(coords[i][0]-coords[x][0]+1)*abs(coords[i][1]-coords[x][1]+1)
                    if area > top_area:
                        top_area = area
        return top_area

    def part_two(self):
        coords = self.input[:]
        top_area = 0
        top_coords = []
        boundaries = self.get_boundaries(coords)
        # self.show_polygon(boundaries)
            
        for i in range(len(coords)):
            for x in range(len(coords)):
                if x > i:
                    area = (abs(coords[i][0]-coords[x][0])+1)*(abs(coords[i][1]-coords[x][1])+1)
                    if area > top_area:
                        if self.is_inside((coords[i], coords[x]), boundaries):
                            # check if any of the rectangle sides are overlapping any other lines, except for the ones near the edges
                            top_coords = (coords[i], coords[x])        
                            top_area = area
        x1, y1 = top_coords[0]
        x2, y2 = top_coords[1]

        # Determine the four corners in clockwise order
        top_left = (min(x1, x2), max(y1, y2))
        top_right = (max(x1, x2), max(y1, y2))
        bottom_right = (max(x1, x2), min(y1, y2))
        bottom_left = (min(x1, x2), min(y1, y2))
        final_rect = [bottom_left, bottom_right, top_right, top_left]
        self.show_polygon([coords, final_rect])
        return top_area

    def get_boundaries(self, polygon):
        boundaries = []
        offset = 0.2
        for i in range(len(polygon)):
            point_a = polygon[i]
            point_b = polygon[(i+1)%len(polygon)]
            prev_point = None
            if len(boundaries) > 0:
                prev_point = boundaries[len(boundaries)-1]
            # check if it's vertical or horizontal line
            if point_a[0] != point_b[0]:
                # horizontal line
                if point_a[0] < point_b[0]:
                    start = (point_a[0]-offset, point_a[1]-offset)
                    end = (point_b[0]+offset, point_b[1]-offset)
                    if start != prev_point and prev_point is not None:
                        new_point = (prev_point[0], start[1])
                        start = new_point
                        boundaries[len(boundaries)-1] = new_point
                    if start[1] != end[1]:
                        print(prev_point)
                        print(start, " ", end)
                        raise Exception("no same y in x line")
                    if prev_point is None:
                        boundaries.append(start)
                    boundaries.append(end)
                else:
                    start = (point_a[0]+offset, point_a[1]+offset)
                    end = (point_b[0]-offset, point_b[1]+offset)
                    if start != prev_point and prev_point is not None:
                        new_point = (prev_point[0], start[1])
                        start = new_point
                        boundaries[len(boundaries)-1] = new_point
                    if start[1] != end[1]:
                        print(prev_point)
                        print(start, " ", end)
                        raise Exception("no same y in x line")
                    if prev_point is None:
                        boundaries.append(start)
                    boundaries.append(end)
            else:
                # vertical line
                if point_a[1] < point_b[1]:
                    start = (point_a[0]+offset, point_a[1]-offset)
                    end = (point_b[0]+offset, point_b[1]+offset)
                    if start != prev_point and prev_point is not None:
                        new_point = (start[0], prev_point[1])
                        start = new_point
                        boundaries[len(boundaries)-1] = new_point
                    if start[0] != end[0]:
                        print(prev_point)
                        print(start, " ", end)
                        raise Exception("no same x in y line")
                    if prev_point is None:
                        boundaries.append(start)
                    boundaries.append(end)
                else:
                    start = (point_a[0]-offset, point_a[1]+offset)
                    end = (point_b[0]-offset, point_b[1]-offset)
                    if start != prev_point and prev_point is not None:
                        new_point = (start[0], prev_point[1])
                        start = new_point
                        boundaries[len(boundaries)-1] = new_point
                    if start[0] != end[0]:
                        print(prev_point)
                        print(start, " ", end)
                        raise Exception("no same x in y line")
                    if prev_point is None:
                        boundaries.append(start)
                    boundaries.append(end)
        return boundaries

    def is_inside(self,edges, boundaries):
        # algorithm: create a list of boundaries, eg. the lines one block from any of the polygon edges, boundary can be defined as (y,x1,x2) or (x, y1,y2)
        # if the rectangle edges ever touch any of the boundaries, then it's not a valid rectangle
        p1, p3 = edges
        p2 = (p1[0], p3[1])
        p4 = (p3[0], p1[1])
        lines = [(p1,p2), (p2,p3), (p3,p4), (p4,p1)]
        
        for i, line in enumerate(lines):
                # horizontal line of rectangle
                for i in range(len(boundaries)):
                    b_start = boundaries[i]
                    b_end = boundaries[(i+1)%len(boundaries)]
                    if self.do_segments_overlap(line, (b_start, b_end)):
                        return False

        return True

    def do_segments_overlap(self, segment_a, segment_b):
        p1,p2 = segment_a
        p3,p4 = segment_b

        t = (p1[0]-p3[0])*(p3[1]-p4[1])-(p1[1]-p3[1])*(p3[0]-p4[0])
        u = (p1[0]-p2[0])*(p1[1] -p3[1])- (p1[1]-p2[1])*(p1[0]-p3[0])
        divisor = (p1[0]-p2[0])*(p3[1]-p4[1]) - (p1[1] -p2[1])*(p3[0] - p4[0])
        if divisor == 0:
            # lines are colinear
            if p1[0] == p2[0] == p3[0] == p4[0]:
                # Overlap along y-axis
                return max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1])
                
            # Check if horizontal
            elif p1[1] == p2[1] == p3[1] == p4[1]:
                # Overlap along x-axis
                return max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0])
            
            # Not vertical or horizontal (unexpected for this function)
            return False
        t_d = t/divisor
        u_d = -u/divisor
        return 0 <= t_d <= 1 and 0 <= u_d <= 1
    
    def check_segments_intersect(self,seg1, seg2):
        (x1, y1), (x2, y2) = seg1
        (x3, y3), (x4, y4) = seg2

        # Check if seg1 is vertical
        if x1 == x2:
            seg1_type = 'vertical'
        elif y1 == y2:
            seg1_type = 'horizontal'
        else:
            raise ValueError("seg1 is not horizontal or vertical")

        # Check if seg2 is vertical
        if x3 == x4:
            seg2_type = 'vertical'
        elif y3 == y4:
            seg2_type = 'horizontal'
        else:
            print(x3, ",", y3)
            print(x4, ",", y4)
            raise ValueError("seg2 is not horizontal or vertical")

        # Case 1: both vertical
        if seg1_type == 'vertical' and seg2_type == 'vertical':
            if x1 != x3:
                return False  # parallel vertical lines
            # Check if y-ranges overlap
            return max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4))

        # Case 2: both horizontal
        if seg1_type == 'horizontal' and seg2_type == 'horizontal':
            if y1 != y3:
                return False  # parallel horizontal lines
            # Check if x-ranges overlap
            return max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4))

        # Case 3: one vertical, one horizontal
        if seg1_type == 'vertical' and seg2_type == 'horizontal':
            # Check if vertical x is within horizontal x-range and horizontal y is within vertical y-range
            return min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2)
        if seg1_type == 'horizontal' and seg2_type == 'vertical':
            return min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4)

        return False  # fallback, shouldn't reach here
    

    def show_polygon(self, polygons):
        # Ensure polygons is a list of polygons
        if all(isinstance(p, (int, float)) for p in polygons[0]):  
            # Single polygon given, wrap it in a list
            polygons = [polygons]

        plt.figure(figsize=(5,5))

        # Colors for multiple polygons
        colors = ['b', 'r', 'g', 'm', 'c']

        for i, polygon in enumerate(polygons):
            x, y = zip(*polygon)
            x = list(x) + [x[0]]  # close polygon
            y = list(y) + [y[0]]

            color = colors[i % len(colors)]
            plt.plot(x, y, color+'-', marker='o', label=f'Polygon {i+1}')
            plt.fill(x, y, color=color, alpha=0.3)

        plt.title("Polygon Visualization")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()


test_file = "2025\\test_inputs\\aoc09.txt"
test_answer_a = 50
test_answer_b = 24
run_file = "2025\\inputs\\aoc09.txt"

input = None
with open(test_file) as input_file:
    input = input_file.readlines()

test_aoc = Aoc(input)
test = test_aoc.part_one()
assert(test_answer_a == test)

with open(run_file) as input_file:
    input = input_file.readlines()

run_aoc = Aoc(input)
answer = run_aoc.part_one()
print(answer)

# test_aoc.show_polygon(test_aoc.input)
test = test_aoc.part_two()
assert(test_answer_b == test)

answer = run_aoc.part_two()
print(answer)
