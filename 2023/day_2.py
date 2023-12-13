import numpy as np

from solver import Solver

class Day2(Solver):
    def day1(self):
        pass
    def day2(self):
        pass


if __name__ == "__main__":
    solver = Day2()
    
    d2_file = "./data/d2.txt"
    solver.read_input(file=d2_file)
    print(f"Part 1: {solver.part1()}")
    print(f"Part 2: {solver.part2()}")