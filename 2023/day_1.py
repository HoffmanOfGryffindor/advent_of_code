import numpy as np

from solver import Solver

class Day1(Solver):
    def part1(self):
        solution = 0
        
        num1 = num2 = None
        for line in self.text:
            num1, _ = self.find_int_val(line)
            num2, _ = self.find_int_val(line[::-1])

            assert num1 and num2 
            solution += int(num1+num2)

        return solution
    
    def part2(self):
        solution = 0

        num1 = num2 = None
        for line in self.text:
            num1_int, num2_int = self.find_int_val(line), self.find_int_val(line[::-1], part2=True)
            str_locations = self.find_str_val(line)
            
            all_locations = str_locations+[num1_int, num2_int]
            filtered = list(filter(lambda x: x != (None, None), all_locations))

            sorted_vals = np.argsort(np.array(filtered, dtype=int)[:, 1])
            (num1, _), *_, (num2, _) = np.array(filtered)[sorted_vals]

            solution += int(num1+num2)

        return solution
                
    def find_int_val(self, line, part2 = False):
        for idx, val in enumerate(line):
            try:
                int(val)
                if part2: idx = (len(line)-1) - idx
                return val, idx
            except: continue
        return None, None

    def find_str_val(self, line):
        num_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        locations = []

        for idx, _ in enumerate(line):
            substr = line[idx:]
            for val, num in enumerate(num_str):
                if substr[:len(num)] == num:
                    # val is the idx location of the number value, idx is the position in the line of text
                    locations.append((str(val), idx))       
        
        if len(locations) == 0: return [(None, None)]
        return locations


if __name__ == "__main__":a
    solver = Day1()
    
    d1_file = "./data/d1p1.txt"
    solver.read_input(file=d1_file)
    print(f"Part 1: {solver.part1()}")
    print(f"Part 2: {solver.part2()}")
    
