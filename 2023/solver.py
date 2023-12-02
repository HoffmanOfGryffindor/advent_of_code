# solver.py is a class that will solve all solutions
from abc import abstractmethod
from numpy import loadtxt

class Solver(object):
    def __init__(self, **kwargs):
        # for k in kwargs.keys():
        #     self.__setattr__(k, kwargs[k]))
        pass
        
    def read_input(self, file):
        self.text = loadtxt(file, dtype=str)

    @abstractmethod
    def part1(self):
        raise NotImplemented
    
    @abstractmethod
    def part2(self):
        raise NotImplemented